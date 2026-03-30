"""
对已有函数增加额外功能，本质是一个闭包函数

特点：
不修改已有函数源代码
不修改已有函数的调用方式
"""
import time


def decrator(func):
    print('进入装饰器模式')

    def check_method():
        print('检查方法')
        func()

    return check_method


def out_method():
    print('实际执行方法')


# 方式一调用装饰器
print(decrator(out_method))


# 方式二：使用注解的方式，在需要装饰的方法上添加装饰器方法的注解
@decrator
def dec_method():
    print("使用注解方式完成")


print(dec_method)


# DEMO1：为使用了装饰器的方法增加输出运行时间
def decrator_time(func):
    def inner():
        start = time.time()
        result = func()
        end = time.time()
        print(f'函数{func.__name__}，执行时间为：{end - start}')
        return result

    return inner

@decrator_time
def time_test1():
    time.sleep(1.5)
    print('实际方法执行完成')

# 带有参数的装饰器
# 装饰器只能接收一个参数，并且为函数类型
# 装饰器外报上一个函数，让最外面函数接收参数，返回装饰器
# DEMO2：
def login(file):
    def login_decorator(func):
        def inner():
            func(file)
        return inner
    return login_decorator

def base_method():
    print('开始执行方法')

if __name__ == '__main__':
    time_test1()
