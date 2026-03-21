# 满足闭包的核心条件
# 1、外部函数中定义一个内部函数
# 2、内部函数使用了外部函数参数
# 3、外部函数返回内部函数

def outer_method(out_param):

    def inner_method(inner_param):
        if type(inner_param)  == str and type(out_param) == str:
            result_str = inner_param + out_param
            return result_str
        elif type(inner_param) == int and type(out_param) == int:
            return inner_param + out_param
        else:
            print(f'外部函数参数：{out_param}，内部函数参数：{inner_param}')
            return inner_param

    return inner_method


pack = outer_method(23)
result = pack(222)

print(result)