class Employee_test():

    def __init__(self, name, age, sex, phone,status):
        self.name = name
        self.age = age
        self.sex = sex
        self.phone = phone
        self.status = status

    def change_status(self, status):
        self.status = status

    # 获取员工整体信息
    def __str__(self):
        print(f'调用 tostring 方法')
        status_str = '离职' if self.status else '在职'
        return f'姓名：{self.name}, 性别, {self.age}, 性别：{self.sex}, 联系方式: {self.phone},任职状态：: {status_str}'


if __name__ == '__main__':
    e1 = Employee_test('琳达', 12, '女', '11111111',False)
    # 对象转为字典,使用__dict__ 或 vars()
    print(e1.__dict__)
    print(vars(e1))

