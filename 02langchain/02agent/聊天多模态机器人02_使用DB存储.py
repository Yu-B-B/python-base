from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory

from my_llm import qwen37

#  提示词模板
prompt = ChatPromptTemplate.from_messages([
    ('system', '你是个乐于助人助手 ，尽力回答你知道的问题，提供的来哦天里是包含 与你对话 用户的相关信息'),
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
        connection ='sqlite:///chat_histories.db'
    )


# 历史消息种类：SystemMessage，HumanMessage，ToolMessage，AIMessage

# 处理历史聊天记录
chain_with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key='input',  # 用户输入消息key
    history_messages_key='chat_history'  # 与提示词模板中定义的内容需要一致（老版本需要保持一致，新版本无所谓）
)

result = chain_with_message_history.invoke(
    {
        'input': '你好 我是夏帆'
    }, {"configurable": {'session_id': 'user_id_123'}}
)

print(result)

result1 = chain_with_message_history.invoke(
    {
        'input': '你好 我的名字是什么'
    }, config={"configurable": {'session_id': 'user_id_123'}}
)
print(result1)
