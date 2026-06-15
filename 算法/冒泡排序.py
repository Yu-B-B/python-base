# 依次比较相邻两个数，当 i > i + 1 下标上的数据时，交换 i 与 i + 1
# 一轮下来，那最后一个数一定是最大的
# 然后再遍历 0 ~ N - i 位置上，确定最大值后放在 N - i 位置上


def bubble_sort(arrs):
    if arrs == [] or len(arrs) < 2:
        return
    
    arrs_len = len(arrs)

    for i in range(0, arrs_len - 1):
        for j in range(0, arrs_len - 1 - i):
            if arrs[j] > arrs[j + 1]:
                # arrs[j + 1], arrs[j] = arrs[j], arrs[j + 1]
                swap(arrs, j, j + 1)
                

def test():
    for i in range(10, -1, -1):
        print(i)
        for j in range(1, 10 - i):
            print(f'内层循环{j}')



def swap(arrs, low, hight):
    temp = arrs[low]
    arrs[low] = arrs[hight]
    arrs[hight] = temp

def print_arr(arrs):
    arrs_len = len(arrs)
    for i in range(0, arrs_len):
        print(f'arrs[{i}]位置上数据为：{arrs[i]}')


arrs = [613,5,1,46,6,1,37,13447,3,723,57,2457,3455,7]
print_arr(arrs)
bubble_sort(arrs)
print_arr(arrs)
# test()