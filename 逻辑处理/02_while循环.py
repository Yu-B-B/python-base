# while 循环结构，一直重复某件事
# todo xiafan random函数失败
# from random import random
#
# device = random.randint(1,999999999)
# step = int(input("请输入步长"))
# num = 0
# while num >= device:
#     num += step
#
# print(f"当前数据为：{device}")
# print(f"结果数据为:{num}")

# 乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        sout = i * j
        print(f'{i}*{j}={sout}', end='\t')
        j += 1
    i += 1
    print(" ")
