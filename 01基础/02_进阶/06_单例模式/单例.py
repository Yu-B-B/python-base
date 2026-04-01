class Person(object):
    def __new__(cls, *args, **kwargs):
        # 采用私有属性，单下划线开关
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

# 第二种方式创建单例
class Student(type):
    def __init__(cls, *args, **keywords):
        cls._instance = None
        super().__init__(*args, **keywords)

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class StudentSingle(object, metaclass=Student):
    pass

if __name__ == '__main__':
    p1 = Person()
    p2 = Person()
    print(p1 == p2)

    p3 = StudentSingle()
    p4 = StudentSingle()
    print(p3 == p4)
