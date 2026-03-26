class Car():
    class_properties_type = '越野车'

    def __init__(self, name):
        self.name = name

    def desc(self):
        print(f'{self.name}牌子的{self.class_properties_type}')


if __name__ == '__main__':
    car1 = Car('JIPU')
    car2 = Car('BEIJING')
    print(car1.desc())
    print(car2.desc())

    print(f'对象1中的全局属性与对象2的全局属性是否相等{car1.class_properties_type == car2.class_properties_type}')

    print(f'修改前car1中的对象：{car1.__dict__}')
    car1.class_properties_type = '轿车'
    print(f'修改后car1中对象：{car1.__dict__}')
    print(f'对象1采用实例修改了全局属性，通过实例访问全局对象内容为：{car1.class_properties_type}')
    print(f'对象1采用实例修改了全局属性，通过类访问全局对象内容为：{Car.class_properties_type}')
    print(
        f'对象1采用实例修改了全局属性，通过实例修改类的全局内容是否生效：{car1.class_properties_type == Car.class_properties_type}')
