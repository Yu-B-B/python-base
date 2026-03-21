def outer_method(params1, params2):
    def inner_method_1(inner_params):
        # 这里重新定义一个变量，而不是覆盖外部函数的变量值
        # params1 = "new Params"
        print(f'闭包函数被调用，外部参数为：{params1},{params2}，内部参数为：{inner_params}')

    return inner_method_1


closure = outer_method(1, 2)

if __name__ == '__main__':

    print(closure.__closure__)
    print(closure.__code__.co_freevars)

    for cell in closure.__closure__:
        print(cell.cell_contents)
