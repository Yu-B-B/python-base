class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, str):
        print(f'{self.name}说了一句：{str}')

if __name__ == '__main__':
    s1 = Student('张三',12)
    s1.speak('啥')
    print(s1.age)