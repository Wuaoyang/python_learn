# -*- coding: utf-8 -*-
'''
@Time    : 2022-10-23 14:33
@Author  : allen
@File    : learn_list.py

'''

'''
    先有商品列表如下
    1. product = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
    需要打印出以下格式：
    --- 商品列表 ---
    0   iphone 6888
    1   MacPro 14800
    2   小米6 2499
    3   Coffee 31
    4   Book 60
    5   Nike 699
    
    2. 根据上面的products列表写一个循环，不断询问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里，最终用户输入q退出时，打印购买的商品列表
'''
product = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]

# 题1
print("--- 商品列表 ---")
for i in range(len(product)):
    detail = product[i]
    print(f"{i}     {detail[0]}    {detail[1]}")

# 题2
# 用java中map的思想，1，2，3，4，5对应5个元组，匹配到就加入购物车咯，没匹配到给提示语即可
# 购物车用一个list存储即可

print("--- 商品列表 ---")
pro_map = {}
for i in range(len(product)):
    detail = product[i]
    pro_map[str(i)] = detail
print(f"商品信息，{pro_map}")
print(f"商品信息，{pro_map.keys()}")

return_list = []
str = "start"
while str != "q":
    str = input("请商品编号，输入q结束：\n")
    if str not in pro_map.keys():
        print("编号查无商品，请重新输入:")
    else:
        return_list.append(pro_map.get(str))
print(f"最终购物车信息为：{return_list}")
