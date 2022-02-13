#!/usr/bin/python
# coding:utf-8

b = 1

while b <= 9:
    a = 1
    while a <= b:
        print("%d * %d = %d" % (a,b,a*b),end= " ")
        a += 1
    print()  #换行
    b += 1