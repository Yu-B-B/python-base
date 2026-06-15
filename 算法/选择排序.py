# 选择排序，遍历数组，找到最小值，与第0号下标上数据交换
# 然后看 1 ~ N -1 位置上，找到最小值，与第一号位置上数据做交换
def select_sort(arrs):
    if arrs == [] or len(arrs) < 2:
        return
    
    arrs_len = len(arrs)
    for i in range(0, arrs_len):
        min_index = i

        for j in range(i, arrs_len):
            min_index = min_index if arrs[min_index] < arrs[j] else j
            j += 1

        if min_index == i:
            continue

        swap(arrs, i ,min_index)
        i+=1

def swap(arrs, low, hight):
    temp = arrs[low]
    arrs[low] = arrs[hight]
    arrs[hight] = temp

def print_arr(arrs):
    arrs_len = len(arrs)
    for i in range(0, arrs_len):
        print(f'arrs[{i}]位置上数据为：{arrs[i]}')

arrs = [5,1,91,19,293,4,5,1,62,67,8,89,9,44,34]
print_arr(arrs)
select_sort(arrs)
print_arr(arrs)