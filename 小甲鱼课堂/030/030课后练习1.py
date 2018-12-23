#!usr/bin/env python
# -*- coding:utf-8 -*-

import os

file_size_dict = dict()
file_all = os.listdir(os.curdir)

for each_file in file_all:
    if os.path.isfile(each_file):
        file_size = os.path.getsize(each_file)
        file_size_dict.setdefault(each_file,file_size)

file_type_list = file_size_dict.keys()
for type_name in file_type_list:
    print('%s 【 %s Bytes】' % (type_name, file_size_dict[type_name]))
