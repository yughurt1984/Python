#!usr/bin/env python
# -*- coding:utf-8 -*-

import os

file_line_position_list = []
line_position_list = []


def search_position(line, keyword):     #找出关键字在行里的位置
    keyword_position_list = []
    position = line.find(keyword)
    while position != -1:     #关键字返回不为空
        keyword_position_list.append(position + 1)
        position = line.find(keyword, position + 1)    #循环查找
    return keyword_position_list        #输出关键字位置列表[1,2,3]


def serch_line(file_name, keyword):      #找出关键字在每个文件夹的行
    f = open(file_name, encoding= 'utf-8')  # 打开查找的文件
    line_num = 0
    line_position_dict = {}

    for each_line in f:
        line_num += 1
        if keyword in each_line:
            line_position_dict.setdefault(line_num, search_position(each_line, keyword))
    f.close()
    return line_position_dict


def search_file(dir_name, keyword, judge):  # 查找txt文件
    txt_file_list = []
    all_file = os.walk(dir_name)
    for i in all_file:
        for each_file in i[2]:
            if os.path.splitext(each_file)[1] == '.txt':  # 找出txt文件
                txt_file = os.path.join(i[0], each_file)
                txt_file_list.append(txt_file)  # 所有txt文件添加列表

    for each_txt_file in txt_file_list:
        line_position_dict = serch_line(each_txt_file, keyword)
        if line_position_dict:
            print('==========================================================')
            print('在文件【 %s 】中找到关键词 %s ' % (each_txt_file, keyword))


        if judge in ['Yes', 'YES', 'yes']:
            line_position_list = line_position_dict.keys()
            for each_line_position in line_position_list:
                print('关键字出现在第 %s 行，第 %s 个位置' % (each_line_position, str(line_position_dict[each_line_position])))




dir_name = input('请输入要查找的目录：')
keyword = input('请输入关键字：')
judge = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：' % keyword)
search_file(dir_name, keyword, judge)



