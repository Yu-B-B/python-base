import  time

from datetime import datetime

# 当前时间戳
print(time.time())

# 英文可读时间
print(time.ctime())

# 也可指定时间戳做时间转换
print(time.ctime(1773583640))

# 时间元组
print(time.gmtime(1773583640).tm_year)

# 格式化时间
print(time.strftime('%y-%m-%d %H:%M:%S', time.localtime(1773583640)))

# 字符串转为时间，转为时间元组
print(f'字符串转时间：{time.strptime('26-03-15 22:07:20','%y-%m-%d %H:%M:%S')}')

# 时间标准库 datetime对象

# 指定时间创建datetime
dt = datetime(2026,8,8,12,1,1)

# 格式化
print(datetime.strftime(dt, '%y-%m-%d %H:%M:%S'))

# 输入日期，计算是该年第几天
input_time = input("请输入日期")
d = datetime.strptime(input_time, '%Y-%m-%d')

days = d.strftime('%j')
print(f'输入的日期为{input_time}，是{d.year} 的第{days}天')
