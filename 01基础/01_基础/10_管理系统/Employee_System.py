import os

from Employee import Employee


class EmployeeManagerSystem():
    sys_file_path = 'employee_data'
    sys_file_backup = 'employee_data_backup'

    def __init__(self):
        self.employee_list = []
        pass

    def main(self):
        """系统入口"""
        # 加载读取员工文件
        self.load_empFile()
        # 进入系统
        while True:
            self.load_sys()

            input_num = input(f'想做的功能')
            if input_num == '7':
                break
            elif input_num == '1':
                self.add_emp()
            elif input_num == '2':
                self.del_emp()
            elif input_num == '3':
                self.change_emp()
            elif input_num == '4':
                self.find_employee()
            elif input_num == '5':
                self.show_all()
            elif input_num == '6':
                self.persist_emp()

    def persist_emp(self):
        write_stream = None
        # 备份原来文件
        if os.path.exists(self.sys_file_backup):
            os.remove(self.sys_file_backup)
        else:
            os.rename(self.sys_file_path, self.sys_file_backup)
        # 创建新文件
        with open(self.sys_file_path, 'w', encoding='utf-8') as f:
            new_list = []
            for employee in self.employee_list:
                new_list.append(employee.__dict__)
            f.write(str(new_list))

        print('写入磁盘')

    def show_all(self):
        for each in self.employee_list:
            print(each)

    def find_employee(self):
        find_name = input('需要查询的人员')
        for each in self.employee_list:
            if each.get_name() == find_name:
                print(each.__dict__)
                break
            else:
                print('未能找到对应人员信息')
        else:
            print('初始化系统中')

    def change_emp(self):
        source_name = input('需要删除的人员姓名')
        target_name = input('请输入目标姓名').strip()

        for each in self.employee_list:
            if each.get_name() == source_name:
                target_name = target_name if target_name else each.get_name()
                each.set_name(target_name)
            else:
                print('未能找到对应员工信息，无法修改')

    def del_emp(self):
        del_name = input('需要删除的人员信息')
        for each in self.employee_list:
            if each.get_name() == del_name:
                self.employee_list.remove(each)
                print('指定内容已被删除 ')
                break
        else:
            print('未能找到相关员工信息\t')

    def add_emp(self):
        name = input('输入员工姓名')
        age = input('输入员工年龄')
        sex = input('输入员工性别')
        phone = input('输入员工联系方式')

        emp = Employee(name, age, sex, phone)
        self.employee_list.append(emp)

    @staticmethod
    def load_sys():
        print('Welcome to employee system!')
        print('---------------------------------------')
        print('1：添加')
        print('2：删除')
        print('3：修改')
        print('4：:查找')
        print('5：展示所有员工')
        print('6：保存员工数据')
        print('7：退出系统')
        print('---------------------------------------')

    def load_empFile(self):
        # 加载数据文件
        read_stream = None
        try:
            read_stream = open(self.sys_file_path, 'r', encoding='utf-8')
        except Exception as e:
            read_stream = open(self.sys_file_path, 'w', encoding='utf-8')

        else:
            content = read_stream.read()
            if content:
                # 将内容作为Python表达式解析
                lst = eval(content)
                for each_content in lst:
                    self.employee_list.append(Employee.from_dict(each_content))
        finally:
            if read_stream:
                read_stream.close()


if __name__ == '__main__':
    emp = EmployeeManagerSystem()
    emp.main()
