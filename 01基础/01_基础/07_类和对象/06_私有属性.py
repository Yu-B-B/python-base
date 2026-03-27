class baseMethod():

    __primaryProperties = 'ha'
    def __init__(self,):
        self.__name = 'name'
        self.__age = 12

    def __primarymethod(self):
        print(f'父类中方法被调用')

    # 通过对外提供公共方法来访问私有属性
    def get_primary_name(self):
        return self.__name

class Child(baseMethod):
    def __init__(self):
        super().__init__()


c1 = Child()
print(f'子类中属性的值为{c1}')
print(f'子类中属性的值为{c1.get_primary_name()}')