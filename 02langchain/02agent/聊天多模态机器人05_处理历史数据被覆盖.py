from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory, RunnablePassthrough
from langchain_community.chat_message_histories import SQLChatMessageHistory

from my_llm import qwen37

"""
摘要保存至保存最后n条以及再次调用大模型的message信息
原对话信息将被覆盖
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

result = final_chain.invoke(
    {
        'input': '你好 我是夏帆','config':{"configurable":{"session_id":"user_id_123"}}
    }, {"configurable": {'session_id': 'user_id_123'}}
)

print(result)

result1 = final_chain.invoke(
    {
        'input': '你好 我的名字是什么','config':{"configurable":{"session_id":"user_id_123"}}
    }, config={"configurable": {'session_id': 'user_id_123'}}
)
print(result1)
