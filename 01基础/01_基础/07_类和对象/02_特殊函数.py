class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, str):
        print(f'{self.name}说了一句：{str}')

    def __new__(cls, *args, **kwargs):
        print('开始创建对象')
        return super().__new__(cls)

    def __str__(self):
        # 这里返回什么，对象调用该方法则拿到什么，未指定时返回对象字节码地址
        return '123123123'

    def __del__(self):
        print(f'开始删除对象，处理逻辑')
        return '对象删除结束'

if __name__ == '__main__':
    s1 = Student('张三',12)
    s1.speak('啥')
    print(s1.age)
    print(s1.__str__())
    print(s1.__del__())