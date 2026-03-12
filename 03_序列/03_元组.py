# 创建的内容不可修改

truple_1 = (2, 1, '122', 122, 122)
truple_2 = (3,)

print(truple_1)
print(truple_1.index(2))
print(f'统计某个数据出现的次数', truple_1.count(122))
print(len(truple_2))
for item in truple_1:
    print(f'遍历元组中内容为：', item)
