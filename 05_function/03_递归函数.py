# 自己调自己

# 阶乘调用
def fun1(a: int) -> int:
    if a == 1:
        return 1
    return a * fun1(a - 1)

print(fun1(6))

