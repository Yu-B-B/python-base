class Animal():
    def speck(self):
        print(f'这是一只动物')

class Dog(Animal):
    def speck(self):
        print(f'狗会狗叫')

class Cat(Animal):
    def speck(self):
        print(f'猫会猫叫')

def common(obj):
    obj.speck()

a = Dog()
b = Cat()

a.speck()
b.speck()