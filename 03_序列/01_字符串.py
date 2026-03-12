# 下标
str1 = '西安人的城墙下西安人的火车\n西安人不管走到哪都不能不吃泡馍'

print(f'输出字符串为: {str1[5]}', end="\n")

# 取前n个字符
print(f'输出字符串为: {str1[:5]}', end="\n")

# 取x-y之间的值，并拆分成z段
print(f'输出字符串为: {str1[0:7:1]}', end="\n")

# 每n步取一个值
print(f'输出字符串为: {str1[::5]}', end="\n")

# 字符串反转
print(f'输出字符串为: {str1[::-1]}', end="\n")

# 大小转换
# 大写：upper;小写：lower；大小写互换：swapcase....

# 字符串对齐
# center 居中展示后剩余位置用 指定字符填充
print(str1.center(45,"*"))

# 分割字符串
# split：切割；partition：分区
# split被切割的不会出现在结果中
print(str1.split("人"))
# partition是按什么做分区，分为左中右
print(str1.partition("人"))
print(str1.partition("城墙上"))

# 合并与替换
print(str1.replace("人","'你在质疑人民'"))

# 判断字符回传类型

# 去除两端多余字符操作