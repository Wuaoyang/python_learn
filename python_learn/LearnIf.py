# -*- coding: utf-8 -*-
'''
@Time    : 2022-10-19 23:02
@Author  : allen
@File    : learn01.py

'''

'''
    结合使用if语句的相关知识，实现石头剪刀布的游戏效果，显示下方提示信息
    请输入：剪刀（0）、石头（1）、布（2）
    用户输入数字0-2中的一个数字，与系统随机生成的数字比较后给出结果信息。
    例如：输入0后，显示如下
    你的输入为：剪刀（0）
    随机生成数字为：1
    哈哈，你输了
'''

import random

# 系统生成数
random = random.randint(0, 2)
input_val = input("请输入:")
if input_val == "0":
    print("你的输入为：剪刀（0）")
    if random == 0:
        print("随机生成数字为：0")
        print("平手")
    elif random == 1:
        print("随机生成数字为：1")
        print("你输了")
    else:
        print("随机生成数字为：2")
        print("你赢了")
elif input_val == "1" :
    print("你的输入为：石头（1）")
    if random == 0:
        print("随机生成数字为：0")
        print("你赢了")
    elif random == 1:
        print("随机生成数字为：1")
        print("平手")
    else:
        print("随机生成数字为：2")
        print("你输了")
elif input_val == "2" :
    print("你的输入为：布（2）")
    if random == 0:
        print("随机生成数字为：0")
        print("你输了")
    elif random == 1:
        print("随机生成数字为：1")
        print("平手")
    else:
        print("随机生成数字为：2")
        print("你赢了")
else:
    print("非法字符")


