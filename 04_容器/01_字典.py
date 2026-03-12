# map转字典

map_1 = {"name": 'zhangsan', 'age': 12, 1: '222'}
map_to_dic = dict(map_1)
print(map_to_dic)

print(map_to_dic["name"])

for key, value in map_to_dic.items():
    print(f'遍历map中得到的key{key}, value:{value}')

print(f'字典中所有的key为{map_to_dic.keys()}')