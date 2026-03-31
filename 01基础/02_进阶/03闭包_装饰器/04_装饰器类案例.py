import os.path
import sys
import time
from functools import wraps


class LoginDoor(object):
    def __init__(self, file):
        self.file = file
        self.login_status = False
        self.users = []
        self.func = None

        self.check_file()

    def check_file(self):
        if os.path.exists(self.file):
            with open(self.file, mode='r') as read_stream:
                lions = read_stream.readlines()
                for lion in lions:
                    user = eval(lion)
                    self.users.append(user)
        else:
            user_choice = input('是否创建新用户：Y/N')
            if user_choice == 'Y' or user_choice == 'y':
                input_user = input('请输入用户名：')
                input_pass = input('请输入密码：')
                with open(self.file, mode='w') as write_stream:
                    user = {'username': input_user, 'password': input_pass}
                    self.users.append(user)
                    write_stream.write(str(user))
            else:
                print('输入指令不正确，即将推出程序')
                time.sleep(2)
                sys.exit(1)

    def __call__(self, func):
        self.func = func

        @wraps(func)  # 保留原函数的元数据
        def wrapper(*args, **kwargs):
            # 未登录时进行登录验证
            if not self.login_status:
                print('请先登录...')
                input_login_user = input('请输入登录账号: ')
                input_login_pass = input('请输入登录密码: ')

                # 验证用户
                login_success = False
                for user in self.users:
                    if (user['username'] == input_login_user and
                            user['password'] == input_login_pass):
                        login_success = True
                        break

                if login_success:
                    self.login_status = True
                    print('登录成功！')
                else:
                    print('用户名或密码错误，无法执行操作')
                    return None

            # 已登录，执行原函数
            return self.func(*args, **kwargs)

        return wrapper

@LoginDoor('store_file')
def need_check_method():
    """需要登录验证的方法"""
    print('执行查询方法')

@LoginDoor('store_file')
def add_data(data):
    """带参数的需要登录验证的方法"""
    print(f'添加数据: {data}')

if __name__ == '__main__':
    print("=== 第一次调用 ===")
    need_check_method()

    print("\n=== 等待2秒后第二次调用 ===")
    time.sleep(2)
    need_check_method()

    print("\n=== 测试带参数的方法 ===")
    add_data("测试数据")