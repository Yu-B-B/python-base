import traceback

try:
    a = 1/0
    print(a)
    num = int("1ss")
except Exception as e:
    print(f'异常详细信息{traceback.format_exc()}')
    print(f'异常缩略信息{e}')


# 抛出异常
def sum():
    try:
         num = int('123s1123')
         raise TypeError('1111')
    except Exception as e:
        print(e)
    finally:
        print('最终结果')
sum()

class PasswordToshortError(Exception):
    def __init__(self, length, default_len):
        self.length = length
        self.default_len = default_len

    def __str__(self):
        return f'输入密码长度为：{self.length}，不能小于{self.default_len}个字符'

def input_pass():
    pwd = input('请输入你的密码')
    if len(pwd) <2:
        raise PasswordToshortError(len(pwd),default_len=6)

if __name__ == '__main__':
    try:
        input_pass()
    except PasswordToshortError as e:
        print(e)