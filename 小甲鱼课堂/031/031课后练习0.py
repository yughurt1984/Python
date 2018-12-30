#!usr/bin/env python
# -*- coding:utf-8 -*-

import pickle
import os
import easygui


content_boy_list = []
content_girl_list = []


def save_file(content_boy_list, content_girl_list, count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'
    pickle_boy_file = open(file_name_boy, 'wb')
    pickle_girl_file = open(file_name_girl, 'wb')
    pickle.dump(content_boy_list, pickle_boy_file)
    pickle.dump(content_girl_list, pickle_girl_file)
    pickle_boy_file.close()
    pickle_girl_file.close()


f = open('D:/学习/python/课后练习/031/record.txt', 'r', encoding= 'utf-8')
count = 0
for each_line in f:
    if each_line[0:6] != '======':
        content = each_line.split(':', 1)
        if content[0] == '小甲鱼':
            content_boy_list.append(content[1])
        if content[0] == '小客服':
            content_girl_list.append(content[1])
    else:
        save_file(content_boy_list,content_girl_list,count)

        count += 1
        content_boy_list = []
        content_girl_list = []

save_file(content_boy_list,content_girl_list,count)
f.close()

