#!/usr/bin/python
# coding:utf-8
import random
import easygui as g
import operator
import os
import sys

global times_guess
times_guess = 0
# 输入并判断输入合法性
def judge_input():
    global input_num
    while True:
        if len(input_num) != 4:
            input_num = g.enterbox(msg='Error:录入的必须为四位数，请重新输入！')
            continue
        if len(set(input_num)) != 4:
            input_num = g.enterbox(msg='Error:录入的必须为不重复数字，请重新输入！')
            continue    
        try:
            int(input_num)
        except ValueError:
            input_num = g.enterbox("Error:录入的必须为数字，请重新输入！")
            continue
        else:
            break
    

def compare(input_num, answer_num_list):
    correct_num = 0
    correct_all = 0
    guess_num_list = []      #把输入的数字拆开,装入列表
    global times_guess
    times_guess += 1
    
    for i in input_num:
        guess_num_list.append(i)
    if operator.eq(guess_num_list, answer_num_list) == True:
        g.msgbox('恭喜你，猜对了！' )
    else:  
        if times_guess >= 7:
            g.msgbox('游戏结束了！')
        else:
            for j in range(0, 4):
                for k in range(0, 4):
                    if (guess_num_list[j] == answer_num_list[k]) and (j != k):
                            correct_num += 1
            for i in range(4):
                if guess_num_list[i] == answer_num_list[i]:
                    correct_all += 1
            feedback = "第 %d 次猜数字了，你的答案是 %dA %dB" % (times_guess, correct_all, correct_num)
            if g.ccbox(feedback, choices=('继续猜', '不猜了')):
                input_num = g.enterbox(msg='请输入一个不重复的四位数:')
                judge_input
                compare(input_num, answer_num_list)
            else:
                g.msgbox('游戏结束了！')  
                os._exit(0)     



answer_num_list = random.sample("123456789", 4)     # 随机数


input_num = ''
judge_input
input_num = g.enterbox(msg='请输入一个不重复的四位数:')
compare(input_num, answer_num_list)