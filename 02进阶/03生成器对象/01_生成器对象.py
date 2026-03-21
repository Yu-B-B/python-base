# 生成器对象也是一种可迭代对象

# 生成器中包含yield关键字

def generator_FUNC():
    v1 = yield 1
    print('hello 1')
    v2  = yield 2
    print(f'第二次传值为:{v2}')
    v3 = yield 3

# 1. yield 把函数变成了一个生成器。
# 2. 调用该函数的时候不会立即执行代码，而是返回了一个生成器对象。
# 3. 当使用 next()（在 for 循环中会自动调用 next()）作用于返回的生成器对象时，函数开始执行，在遇到 yield 的时候会『暂停』，并返回当前的迭代值；
# 4. 当再次使用 next() 的时候，函数会从原来『暂停』的地方继续执行，直到遇到 yield 语句，如果没有 yield 语句，则抛出异常；
# 5. 生成器函数的执行过程看起来就是不断地 = 执行->中断->执行->中断的过程
# 6. send() 函数就是 next() 的功能，加上传值给上次暂停的 yield。
# 7. close() 函数来关闭一个生成器。生成器被关闭后，再次调用 next() 函数，不管能否遇到 yield 关键字，都会抛出 StopIteration 异常。

g = generator_FUNC() # 创建生成器
# 判断对象中是否包含xx函数
print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))

# next函数是依次返回yield后修饰的内容
print(next(g))
# send方法将值传给函数内部使用后再返回后面的值
print(g.send(5))
print(g.send(12))


#