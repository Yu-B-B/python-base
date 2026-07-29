from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory, RunnablePassthrough
from langchain_community.chat_message_histories import SQLChatMessageHistory
import gradio as gr

from my_llm import qwen37

"""
摘要保存至保存最后n条以及再次调用大模型的message信息
原对话信息将被覆盖，虽然历史消息被摘要后可能 使用不到，但也能被保存
06。使用gradio库完成可视化
"""
#  提示词模板
prompt = ChatPromptTemplate.from_messages([
    ('system', '{system_message}'),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ('human', '{input}')
])

chain = prompt | qwen37

# 存储聊天记录（内存 / 关系型数据库）

# 使用字典格式保存不同用户的聊天记录
store = {}


# 定义工厂func，告诉大模型怎么存储与怎么返回历史记录
def get_session_history(session_id: str):
    """
    从内存存储的历史消息列表中，返回当前会话的所有历史消息
    """
    return SQLChatMessageHistory(
        session_id=session_id,
        connection='sqlite:///chat_histories.db'
    )


# 历史消息种类：SystemMessage，HumanMessage，ToolMessage，AIMessage

# 处理历史聊天记录
chain_with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key='input',  # 用户输入消息key
    history_messages_key='chat_history'  # 与提示词模板中定义的内容需要一致（老版本需要保持一致，新版本无所谓）
)


# 剪辑摘要上下文 ，历史记录：保留最近n条数据
def summarize_messages(current_input: str):
    """
    剪辑摘要上下文
    """
    session_id = current_input['config']['configurable']['session_id']
    if not session_id:
        raise ValueError('需通过config参数提供session_id')

    # 获取当前对话的历史消息
    chat_history = get_session_history(session_id)
    stored_messages = chat_history.messages

    if len(stored_messages) <= 2:
        return {"original_message": stored_messages, "summary": None}
        # return False

    # 超过的数据进行摘要,保留最后两条消息，之前的消息生成摘要
    last_message_history = stored_messages[-2:]
    messages_to_summarize = stored_messages[:-2]

    summarization_prompt = ChatPromptTemplate.from_messages(
        [
            ('system', '将一下对话历史压缩为一条保留关键信息的摘要信息'),
            ('placeholder', '{chat_history}'),
            ('human', '请生成包含上述对话核心内容的摘要，保留重要事实和决策')
        ]
    )

    summarization_chain = summarization_prompt | qwen37
    # 生成摘要
    summary_message = summarization_chain.invoke({'chat_history': messages_to_summarize})

    # 重构历史聊天记录
    # chat_history.clear() # 这里将清除历史聊天记录，影响摘要后查询历史信息
    # chat_history.add_message(summary_message)
    # for msg in last_message_history:
    #     chat_history.add_message(msg)

    # 返回摘要与后续结果
    return {  # 最终返回n+1条消息，n为
        'original_message': last_message_history,
        'summary': summary_message,
    }

    return True


# 最后需要的链
final_chain = RunnablePassthrough.assign(
    messages_summarized=summarize_messages
) | RunnablePassthrough.assign(
    input=lambda x: x['input'],
    chat_history=lambda x: x['messages_summarized']['original_message'],
    system_message=lambda x: f"你是个乐于助人助手 ，尽力回答你知道的问题，摘要：{x['messages_summarized']['summary']}" if
    x['messages_summarized'].get('summary') else '无摘要'
) | chain_with_message_history


# result = final_chain.invoke(
#     {
#         'input': '你好 我是夏帆','config':{"configurable":{"session_id":"user_id_123"}}
#     }, {"configurable": {'session_id': 'user_id_123'}}
# )
#
# print(result)
#
# result1 = final_chain.invoke(
#     {
#         'input': '你好 我的名字是什么','config':{"configurable":{"session_id":"user_id_123"}}
#     }, config={"configurable": {'session_id': 'user_id_123'}}
# )
# print(result1)

# 按钮确认提交消息，输入包含历史聊天内容以及当前输入框中内容
def click_submit(chat_history, user_message):
    # 向聊天记录中添加消息
    if user_message:
        chat_history.append({'role': 'user', 'content': user_message})
    return chat_history, ''


def chain_invoke(chat_history):
    last_message_input = chat_history[-1]
    aimessage_result = final_chain.invoke(
        {
            'input': last_message_input['content'], 'config': {"configurable": {"session_id": "user_id_123"}}
        }, config={"configurable": {'session_id': 'user_id_123'}}
    )
    chat_history.append({'role': 'assistant', 'content': aimessage_result.content})
    return chat_history


# 读取 音频文件
def audio_input_read(audio_msg):
    print(chain_with_message_history)
    # if audio_msg:
    #     client =  ZhipuAI(api_key='')
    #     with open(audio_msg, 'rb') as f:
    #         resp =  client.audio.transcriptions.create(
    #             model =  'glm-asr',
    #             file =  audio_msg,
    #             stream = False
    #         )
    #         text = resp.model_extra['text']
    #         return text
    # return ''


with (gr.Blocks(title='多模态聊天机器人') as block):
    chatbot = gr.Chatbot(height=500, label='聊天机器人')

    # 行组件
    with gr.Row():
        # 左边输入文字
        with gr.Column(scale=4):
            user_input = gr.Textbox(placeholder="请输入发送的消息...", label='文字输入', max_lines=6)

            submit_btn = gr.Button('发送', variant='primary')

        with gr.Column(scale=1):
            audio_input = gr.Audio(sources=['microphone'], label='请录入音频', type='filepath', format='wav')

    # 提交事件，将当前信息做保存
    user_submit_content = user_input.submit(click_submit, [chatbot, user_input], [chatbot, user_input])

    # 调用大模型
    user_submit_content.then(chain_invoke, chatbot, chatbot)

    # 语音录制
    audio_input.change(audio_input_read, [audio_input], [user_input])

    # 提交按钮点击事件
    submit_btn.click(click_submit, [chatbot, user_input], [chatbot, user_input]
                     ).then(chain_invoke, chatbot, chatbot)
    pass

if __name__ == '__main__':
    block.launch(theme=gr.themes.Soft())
