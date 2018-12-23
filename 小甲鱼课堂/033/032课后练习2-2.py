#!usr/bin/env python
# -*- coding:utf-8 -*-

try:
    with open('My_File.txt') as f: # 当前文件夹中并不存在"My_File.txt"这个文件T_T
        print(f.read())
except OSError as reason:
    print('出错啦：' + str(reason))
