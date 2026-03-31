# 将方法当作属性使用
# property只能修饰那些返回私有属性的内容
class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    # 使用set方法时，要先保证存在被property修饰的内容，如下面这个setter，需要存在一个被property修饰的age方法
    @age.setter
    def age(self, new_age):
        self.__age = new_age


p = Person('123',333)
print(p.name)
print(p.age)