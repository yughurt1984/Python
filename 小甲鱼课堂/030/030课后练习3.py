#!usr/bin/env python
# -*- coding:utf-8 -*-

import os

av = []
av_type = ['.avi', '.mp4', '.rmvb']


def search_file(dir_name):
    os.chdir(dir_name)
    file_all = os.listdir(os.curdir)  # 遍历地址列表中全部文件
    for each_file in file_all:
        if os.path.splitext(each_file)[1] in av_type:  # 判断文件名是否存在
            av.append(os.getcwd() + os.sep + each_file + '\n')

        if os.path.isdir(each_file):
            search_file(each_file)
            os.chdir(os.pardir)


start_dir = input('请输入要查找的目录：')
search_file(start_dir)

av_file = open('videoList.txt', 'w', encoding='utf-8')
av_file.writelines(av)
av_file.close()
