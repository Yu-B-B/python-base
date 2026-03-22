# 迭代器对象：包含__iter__与 __next__
class MyIterator:

    def __init__(self, num):
        self.num = num
        self.counter = -1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.num += 1
        if self.num == self.counter:
            raise StopIteration
        return self.num


# for 循环本质
# 使用 __iter__ 找到迭代器对象
# 拿到迭代器对象后一直调用__next__
# 在调用__next__时捕获StopIteration异常



# 可迭代对象：
# 一个类中包含__iter