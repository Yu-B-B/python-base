# 基础表达式
# sys_input_core = input("请输入你的分数：")
# convert_core = int(sys_input_core)
# if convert_core > 680:
#     print("上清华")
# elif 680 > convert_core > 340:
#     print("川大")
# else:
#     print("家里蹲")


# 嵌套if
# permission = bool(input("请输入当前权限："))
# age = int(input("请输入你的年龄："))
# if permission:
#     print("当前有权限")
#     if 18 > age > 35:
#         print("可以开始打工")
#     elif age >= 35:
#         print('还在打工啊')
#     else:
#         print('非法雇佣童工')
# else:
#     print("没有权限，跳出")

# 三目运算
input_ = input("请输入一个数字：")
try:
    sys_input_num = int(input_)
    result = f'当前数字:{sys_input_num} 为偶数' if sys_input_num % 2 == 0 else f'当前数字:{sys_input_num}为奇数'
    print(result)
except NameError:
    print("参数类型错误")