# set中元素不可重复，不可变类型的可变散列容器
# 所以Set中只能放入常量，元组

set1 = {'set1', 'set2', 'set3', 'set3'}
print(set1)

# add
set1.add(12)
print(set1)


# 删除
set1.remove(12)
print(set1)

# 遍历
for item in set1:
    print(item)

