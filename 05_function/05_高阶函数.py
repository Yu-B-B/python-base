# 把函数作为参数传递
# 函数的参数是函数
from functools import reduce


def fun1(a=0):
    return abs(a)


def fun2(c, d, method):
    return method(c) + method(d)


# 使用fun1()表示是将方法的返回结果作为参数传递，在方法内部调用时，翻译出来就是想在常量上调用函数
# print(fun2(-3, -5, fun1()))

# 正确的调用方式为
print(fun2(-4, -5, fun1))


# 2、函数的返回值为函数
def fun3(*args):
    def fun3_1():
        a = 0
        for arg in args:
            a += arg
        return a

    return fun3_1


print(fun3(1, 2, 3))
print(fun3(1, 2, 3)())

# 3、map函数，接受一个函数和多个可迭代对象，再将对象中每一个元素处理后返回迭代器
# 普通函数方式：
numbers = [1, 2, 4, 5, 6, 7]


def fun4(a):
    return a * a


print(f'普通函数调用方法后：{map(fun4, numbers)}')
print(f'普通函数调用方法,转为数据后：{list(map(fun4, numbers))}')

# map高阶
map_result = map(lambda a: a ** 2, numbers)
print(f'python内置函数调用后{list(map_result)}')


# reduce：python中内置函数，将对象中内容反复调指定函数
def fun5(a, b):
    return a + b


reduce_result = reduce(fun5, numbers)

print(reduce_result)

# 类似方式·
reduce_lambda_result = reduce(lambda x, y: x + y, numbers)
print(reduce_lambda_result)

# reduce案例: 统计字符串中每个词出现的次数
str_word = "The library changes include significantly improved capabilities for introspection in asyncio, support for Zstandard via a new compression.zstd module, syntax highlighting in the REPL, as well as the usual deprecations and removals, and improvements in user-friendliness and correctness"
# 1、拆分句子为数组
str_word_split = str_word.split()
# 2、将数组转为map，给每个单词赋初始值。一个map中包含键值对字典
str_word_map = map(lambda word: {word: 1}, str_word_split)
# 3、遍历map，map不是字典类型本身，没有提供items()方法，直接遍历即可
word_count_map = {}

def reduce_map_count(params):
    for map_dict in params:
        for key,value in map_dict.items():
            keys = word_count_map.keys()
            if key in keys:
                word_count_map[key] += value
            else:
                word_count_map[key] = value
    return word_count_map


print(reduce_map_count(str_word_map))
