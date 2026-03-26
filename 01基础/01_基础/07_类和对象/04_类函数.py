# 类函数与成员函数的区别
# 成员函数的第一个参数都是self
# 类函数的第一个参数为cls，且方法上采用@classmethod装饰器修饰

# 静态函数。方法既不需要使用实例对象（无self参数），也不需要使用类对象（无cls参数），可定义静态函数

class Table():
    table_name = '方桌'

    # 成员函数
    def __init__(self):
        self.table = []

    def describe(self):
        print('这张桌子有四条腿')

    @classmethod
    def class_method(cls, width=10, length=20):
        print(f'这张{cls.table_name}的长度为：{length}，宽度为：{width}')

    @staticmethod
    def static_method():
        print('这是个静态函数')

if __name__ == '__main__':
    table = Table()

    table.describe()
    table.class_method(5, 2)

    Table.class_method(10, 39)

# 静态函数也可以通过实例 或 类两种方式调用