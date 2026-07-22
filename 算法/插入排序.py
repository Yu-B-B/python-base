# 插入排序
# 认为前 i 个数是有序的，关注 i+1 上的数据，当 i > i+1 时，交换 i 与 i+1 的位置
# 当 i 

def insert_sort(arrs):
    if arrs == [] or len(arrs) < 2:
        return
    
    arrs_len = len(arrs)
    for i in range(0, arrs_len - 1):
        next_index = i
        while next_index >= 0 and arrs[next_index] > arrs[next_index + 1]:
            arrs[next_index], arrs[next_index + 1] = arrs[next_index + 1], arrs[next_index]
            next_index -= 1

            
def print_arr(arrs):
    arrs_len = len(arrs)
    for i in range(0, arrs_len):
        print(f'arrs[{i}]位置上数据为：{arrs[i]}')

arrs = [5,1,91,19,293,4,5,1,62,67,8,89,9,44,34]
print_arr(arrs)
insert_sort(arrs)
print_arr(arrs)