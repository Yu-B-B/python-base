class Employee():
    __name = None
    __age = None
    __sex = None
    __phone = None
    # 是否离职，
    __status = False

    def __init__(self, name, age, sex, phone):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__phone = phone

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def change_status(self, status):
        self.__status = status

    @classmethod
    def from_dict(cls, data):
        """从字典创建Employee对象"""
        name = data.get('_Employee__name')
        age = int(data.get('_Employee__age', 0))
        sex = data.get('_Employee__sex')
        phone = data.get('_Employee__phone')

        # 创建对象
        emp = cls(name, age, sex, phone)

        # 处理状态（如果有）
        if '_Employee__status' in data:
            emp.change_status(data['_Employee__status'])

        return emp

    # 获取员工整体信息
    def __str__(self):
        print(f'调用 tostring 方法')
        status_str = '离职' if self.__status else '在职'
        return f'姓名：{self.__name}, 性别, {self.__age}, 性别：{self.__sex}, 联系方式: {self.__phone},任职状态：: {status_str}'


if __name__ == '__main__':
    e1 = Employee('琳达', 12, '女', '11111111')
    # 对象转为字典,使用__dict__ 或 vars()
    # 输出内容为：{'_Employee__name': '琳达', '_Employee__age': 12, '_Employee__sex': '女', '_Employee__phone': '11111111'}
    # 因这些内容都是私有变量，Python 会自动将 __name 改为 _类名__name，以避免子类意外覆盖私有属性
    print(e1.__dict__)
    print(vars(e1))

    # 输出：姓名：琳达, 性别, 12, 性别：女, 联系方式: 11111111,任职状态：: 在职
    #
    print(e1)
