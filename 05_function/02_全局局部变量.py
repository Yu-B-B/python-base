# 局部变量，只能用在方法内部，不可越权
# 全局变量

# 在方法调用中，相同方法中，每多一个参数调用，那么函数将开辟新的堆空间进行存储
def fun1(a, b=[4, 5]):
    if a not in b:
        b.append(a)
    return b


print(fun1(1))
print(fun1(1, [45]))
print(fun1(3))
print(fun1(6))
