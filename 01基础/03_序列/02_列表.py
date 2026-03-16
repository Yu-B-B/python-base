# 存储同种类型的数据
str_list = ['Python', '3.14', 'is', 'the', 'latest', 'stable', 'release', 'of', 'the', 'Python', 'programming',
            'language,', 'with', 'a', 'mix', 'of', 'changes', 'to', 'the', 'language,', 'the', 'implementation,', 'and',
            'the', 'standard', 'library.', 'The', 'biggest', 'changes', 'include', 'template', 'string', 'literals,',
            'deferred', 'evaluation', 'of', 'annotations,', 'and', 'support', 'for', 'subinterpreters', 'in', 'the',
            'standard', 'library.']

print(str_list.count("Python"))
print(str_list.index('of'))

print(len(str_list))

# add
str_list.append("HEI")
print(len(str_list))

str_list.insert(4, "HHHH")
print(len(str_list))

# 在结尾追加序列，序列将平铺追加
str_list.extend("HEI")
print(str_list)

# 遍历
for i in str_list:
    print(i)