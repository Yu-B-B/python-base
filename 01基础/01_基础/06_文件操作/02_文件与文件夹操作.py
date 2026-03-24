import os

print(f'当前文件工作目录：{os.getcwd()}')



input_file = input('需检查文件路径的为：')
print(f'文件{input_file}的相对路径为：{os.path.abspath(input_file)}')

print(f'文件{input_file}文件大小为：{os.path.getsize(input_file)}')

print(f'拆分得到文件的路径为：{os.path.split(os.path.abspath(input_file))}')


input_path = input('需要检查的文件夹目录：')
print(f'当前目录{input_path}下存在的文件及有{os.listdir(input_path)}')