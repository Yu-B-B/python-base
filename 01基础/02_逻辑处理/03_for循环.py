# range函数，左闭右开

res = 0

# for i in range(1, 10, 2):
#     print(i)


# 写法2
for j in range(100):
    if j % 3 == 0:
        res += j

# break
# for i in range(100):
#     # 这里的break会跳出当前循环
#     if i == 20:
#         break
#     elif i % 3 == 0:
#         res += i


# continue
# for i in range(100):
#     if i % 2 == 0:
#         continue
#     elif i % 3 == 0:
#         res += i
print(res)