str1 = "Hello"
print(str1)

str2 = 'World'
print(str2)

str3 = """
 现在AI兴起
 正是学AI的好时机
"""
print(str3)

str4 = "It’s a huge pig"
print(str4)

# 转义字符
str5 = 'It\'s a big problem'
print(str5)

str6 = "\t好看的话，\n\t记得一键三连，点赞投币哦"
print(str6)

# 字符串拼接
str1_2 = str1 + str2
print(str1_2)

# 占位
str_error = "1231234sdf"
str_detail = "三方调用异常"
print("系统错误：%s，错误原因 %s"% (str_error, str_detail))

# 格式化
name = "张三"
print(f"adkfkasdfjl{name}")