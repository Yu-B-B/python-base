import os

def iterator(file_path):
    if not os.path.exists(file_path):
        return 0
    if os.path.isfile(file_path):
        return 1
    
    stack = [file_path]
    result = 0
    while stack:
        current = stack.pop()
        try:
            for item in os.listdir(current):
                full_path = os.path.join(current)
                if os.path.isfile(full_path):
                    result += 1
                elif os.path.isdir(full_path):
                    stack.append(full_path)
        except PermissionError:
            pass
    return result


path = 'D:\develop\web'
reuslt = iterator(path)
print(reuslt)