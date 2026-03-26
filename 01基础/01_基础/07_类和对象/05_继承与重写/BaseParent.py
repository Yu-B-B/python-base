class Person():
    name = '人'

    def sport(self):
        print('跳一下')


class Car():
    name = '车'

    def sport(self):
        print("车开起来了")


# 单继承时，该子类拥有父类的所有属性。多继承时，若属性重复，先拥有第一个继承对象中内容
class JapanPerson(Person, Car):
    def say(self):
        print('小日本说八嘎话')

    def sport(self):
        print('小八嘎的车动起来了')


jp = JapanPerson()
# 当子类中不存在与父类相同的方法时，调用父类中方法。当子类中存在与父类相同方法时，为重写
jp.sport()


print(jp.name)

print(f'对象JP是否为父类类型：{isinstance(jp, JapanPerson)}')

print(f'是否存在继承关系：{issubclass(JapanPerson, Person)}')

print(f'所有类都继承Object：{issubclass(JapanPerson, Person)}')
