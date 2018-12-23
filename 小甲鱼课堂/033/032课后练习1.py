#!usr/bin/env python
# -*- coding:utf-8 -*-

import random


global guess
def int_input(prompt=''):
    while True:
        try:
            int(input(prompt))
            break
        except ValueError:
            print('Error：输入的必须为数字！')
    else:
        guess = int(int_input('不妨猜一下小甲鱼现在心里想的是哪个数字：'))


secret = random.randint(1, 10)
print('------------------我爱鱼C工作室------------------')

guess = int_input('不妨猜一下小甲鱼现在心里想的是哪个数字：')
while guess != secret:
    guess = int_input('请重新输入：')
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
print("游戏结束，不玩啦^_^")

