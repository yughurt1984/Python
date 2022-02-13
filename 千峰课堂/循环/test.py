#!/usr/bin/python
# coding:utf-8

layer = 1


while layer <= 5:
    count = 1
    while count <= layer:
        print("*",end= "")
        count += 1
    print()  #换行
    layer += 1
