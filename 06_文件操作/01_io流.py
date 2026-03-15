# python中输入与输出统称为IO流
# 读取文件的访问格式
# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

# 打开文件流
file_stream = open('IO_DEMO_FILE.txt', mode='r', encoding='utf-8')

# 读取文件，
print(f'读取整个文件：{file_stream.read()}', end='\n')

# 移动指针位置，0开头、1当前位置、2文件结尾位置
file_stream.seek(0)

# 读取指定长度，若在上个读完的位置后读取指定长度，需要重置文件指针
print(f'读取指定长度内容：{file_stream.read(5)}', end='\n')

# 一行一行的读取
file_stream.seek(0)

print(f'读取指定行数内容：{file_stream.readline()}', end='\n')
print(f'读取第二行 内容：{file_stream.readline()}', end='\n')

file_stream.seek(0)

# 写操作
write_file_stream = open('IO_DEMO_FILE.txt', mode='w', encoding='utf-8')

write_file_stream.write('新写入的一行内容')

for item in range(100):
    print(f'当前指针位置在{write_file_stream.tell()}', end='\n')
    write_file_stream.seek(0, 2)
    write_file_stream.write(str(item))

write_file_stream.close()
