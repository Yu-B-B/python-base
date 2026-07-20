from typing import Optional

from langchain_core.tools import tool
from langchain.agents import create_agent
from pywin.framework.toolmenu import tools

from models.my_llm import qwen35


# Optional修饰表示当前参数可选
@tool
def get_employee_info(employee_id: Optional[str] = None,
                      email: Optional[str] = None) -> str:
    # 需要增加描述，用来告诉大模型这个工具是用来做什么的，每个参数的作用（Args中描述）
    """
    Args:
        employee_id：员工 ID （可选）
        email:邮箱地址 （可选  ，支持 部分 匹配 ，如 ”wangyu“，”gmail.com","163.com"
    Returns:
        str:员工信息
    """

    mock_employee_database = {
        "E001": {"name": "张三", "department": "技术部", "position": "软件工程师", "email": "zhangsan@gmail.com"},
        "E002": {"name": "里斯", "department": "技术部", "position": "软件工程师", "email": "lisi@gmail.com"},
        "E003": {"name": "老六", "department": "技术部", "position": "软件工程师", "email": "laoliu@gmail.com"}

    }

    if employee_id:
        employee_record = mock_employee_database.get(employee_id)

        if employee_record:
            return f"员工{employee_id}的信息为：姓名：{employee_record['name']}，部门：{employee_record['department']}，岗位：{employee_record['position']}，邮箱：{employee_record['email']}"
        else:
            return f"员工ID{employee_id} 不存在 "

    if email:
        results = []
        for id, info in mock_employee_database.items():
            if email.lower() in info["email"].lower():
                results.append(
                    f"员工{employee_id}的信息为：姓名：{info['name']}，部门：{info['department']}，岗位：{info['position']}，邮箱：{info['email']}")
        if results:
            return "找到以下员工：\n" + "\n".join(results)
        else:
            return f"未找到邮箱包含 '{email}' 的员工"

    return "请提供 employee_id 或 email 至少一个参数。"


# 创建Agent
agent = create_agent(
    model=qwen35,
    tools=[get_employee_info],
    system_prompt="你是个员工信息查询助手，可以查询员工姓名、部门、职务和邮箱"
)

result = agent.invoke({"messages": [{"role": "user", "content": "查询员工邮箱包含lisi的用户信息"}]})
print(type(result))
print(result)
print(result["messages"][-1].content)
