"""
通过 class 属性就能创建一个类对象
所有类对象隐式继承object类

type为所有对象的顶点，所有对象都创建自type
object为类继承顶点，所有类都继承自object

"""


# 正常创建类对象
class Student(object):
    def __init__(self, name):
        self.name = name


s1 = Student('sss')

s2 = type('Student', (object,), {'name': 'lisi'})

print(s1.name)
print(s2.name)

print(s1.__class__ == s2.__class__)
