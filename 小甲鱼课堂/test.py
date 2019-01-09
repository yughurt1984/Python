#!/usr/bin/python
# coding:utf-8

import random

dict1 ={'0': [9, 5], '1': [6, 10],'2': [10, 1], '3': [9, 3], '4': [3, 9], '5': [2, 5], '6': [1, 4], '7': [7, 3], '8': [10, 4], '9': [9, 2]}
keys = []

position = [10,4]

if position in dict1.values():
    dictItem = dict1.items()
    for i in dictItem:
        if position == i[1]:
           dict1.pop(i[0])
print(dict1)
        