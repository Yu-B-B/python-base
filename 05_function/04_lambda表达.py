me = lambda x: x * 2

print(me(3))

# 现在有一数组对象，对某一字段排序
dic = [{'name': 'zhangsan', 'age': 18},
       {'name': 'lisi', 'age': 56},
       {'name': 'wangwu', 'age': 32}]

dic.sort(key=lambda each: each['age'])

print(dic)