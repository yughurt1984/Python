#!usr/bin/env python
# -*- coding:utf-8 -*-

import os

input_name = input('请输入要查找的文件名：')
address = input('请输入要查找的目录：')
address_list = []
fold_address_dict = {}
result_dict = {}

file_all = os.listdir(address)  # 遍历地址列表中全部文件
for each_file in file_all:
    if each_file == input_name:  # 判断文件名是否存在
        result_dict.setdefault(each_file, each_address)
        else:
            fold_address = address + '/' + each_file
            continue
address = fold_address

result_list = result_dict.keys()
print(result_list)
for each_result in result_list:
    print(result_dict[each_result] + '\\' + each_result)
