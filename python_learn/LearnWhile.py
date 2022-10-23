# -*- coding: utf-8 -*-
'''
@Time    : 2022-10-19 23:36
@Author  : allen
@File    : learn_while.py

'''

# 题目 0-100求和

sum = 0
index = 0
while index <= 100:
    sum += index
    index += 1
print(f"0-100求和结束，结果为{sum}")

sum = 0
for i in range(101):
    sum += i
print(f"0-100求和结束，结果为{sum}")

