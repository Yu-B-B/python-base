import os.path
import sys
import time
from functools import wraps


def login_door(file):
    def login(func):
        login_status = False
        users = []
        # 检查文件是否存在
        is_exists = os.path.exists(file)
        if is_exists:
            with open(file) as read_stream:
                lions = read_stream.readlines()
                for lion in lions:
                    user = eval(lion)
                    users.append(user)
        else:
            choice = input('是否需要创建新用户：Y/N')
            if choice == 'Y' or choice == 'y':
                with open(file, mode='w') as write_stream:
                    username = input('请输入用户名：')
                    password = input("请输入密码：")
                    user = {'username': username, 'password': password}
                    users.append(user)
                    write_stream.write(str(user))
            else:
                print('当前用户选择退出')
                sys.exit()

        # 使用 wraps 伪装调用时让外面知道还有内置的方法
        @wraps(func)
        def inner(*args, **kwargs):
            nonlocal login_status
            if not login_status:
                input_user = input('登录用户名：')
                input_pass = input('登录用户名：')
                for un in users:
                    if un['username'] == input_user and un['password'] == input_pass:
                        login_status = True
                        print('登录成功')
                        break
                    else:
                        print('输入用户名密码有误')
            if login_status:
                return func(*args, **kwargs)
            return None

        return inner

    return login


@login_door('store_file')
def need_check_method():
    print('执行查询方法')


if __name__ == '__main__':
    # 实际先调用装饰器函数中inner方法
    need_check_method()
    time.sleep(2)
    need_check_method()
