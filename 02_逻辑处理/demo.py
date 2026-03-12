# 猜数游戏，每次从1-100中取整数，每一轮可以猜2次
# 一轮结束后输入yes可继续玩耍，输入no推出
import random

pc = 0
flag = True
while flag:
    title = input("是否开始下庄：")
    if title == 'yes' or title == 'y':
        # 每轮猜几次
        each_time = int(input("想要压几次："))
        current_num = random.randint(1, 100)
        current_input = int(input("请输入想压的点数："))
        print("\t")
        for i in range(each_time):
            if current_input == current_num:
                print("恭喜你猜中啦！！，本次庄家点数为", current_num)
                break
            elif i == each_time - 1:  # 最后一次机会
                print(f"很遗憾，都错了，庄家点数为：{current_num}")
            elif current_input > current_num:
                current_input = int(
                    input(f"很遗憾，猜错了，庄家点数比你的小，还剩{each_time - i}次，请重新输入："))
                continue
            else:
                current_input = int(input(
                    f"很遗憾，猜错了，庄家点数比你的大，还剩{each_time - i}次,请重新输入："))
                continue
        else :
            pass
        pc += 1
        pass
    elif title == 'no' or title == 'n':
        print(f"本次在赌场共计游玩{pc}次")
        break
    else:
        print('指令错误')
