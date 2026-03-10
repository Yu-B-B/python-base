# 获取键盘输入
# sys_input = input("请输入姓名：")
# sys_input_age = input("请输入年龄：")
#
# print(f"输入的年龄为{sys_input_age}，姓名为：{sys_input}")

# 取钱
sys_amount = 10000
sys_input = input("需要取出的钱为：")
print("----------------------")
print(type(sys_input))

# 类型转换 类似java
sys_account = sys_amount - int(sys_input)
print(f"取钱后，余额为：{sys_account}")