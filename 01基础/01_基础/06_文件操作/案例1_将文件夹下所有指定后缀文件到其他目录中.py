import os


# 将该目录中所有指定文件拷贝到另一个指定目录中
# 目录下还有子目录

def copy_dir(src, dst, filetype):
    count = 0
    for each_name in os.listdir(src):
        # 拿到当前路径，拼接完整路径
        this_dir_path = os.path.join(src, each_name)
        if os.path.isfile(this_dir_path) and each_name.endswith(filetype):
            # 拷贝到指定目录，且保持目录完整性
            if not os.path.exists(dst):
                os.makedirs(dst)
            dst_full_path = os.path.join(dst, each_name)
            num = copy_files(this_dir_path, dst_full_path)
            count += num
        elif os.path.isdir(this_dir_path):
            # 若还是目录，这里需要维持现在目录的路径
            new_path = os.path.join(dst, each_name)
            copy_dir(this_dir_path, new_path, filetype)
    return count


def copy_files(src, dst):
    # 针对小文件，可使用with语句短暂打开
    # with open(src, 'r', encoding='utf-8') as f:
    #     content = f.read()
    #     with open(dst, 'w', encoding='utf-8') as dst_f:
    #         dst_f.write(content)

    # 针对大文件
    open_stream = open(src, 'r', encoding='utf-8')
    write_stream = open(dst, 'w', encoding='utf-8')
    while True:
        content = open_stream.read(1024*10)
        if not content:
            break
        write_stream.write(content)
    open_stream.close()
    write_stream.close()
    return 1


if __name__ == '__main__':
    source_path = input('需要检索的文件夹地址：')
    target_path = input('复制文件到指定的位置：')
    target_file_type = input('文件类型为：')
    copy_dir(source_path, target_path, target_file_type)
