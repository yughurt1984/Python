#!usr/bin/env python
# -*- coding:utf-8 _*-

old = open('D:/学习/0基础学Python/029一个任务/课后练习/old.txt','r', encoding= 'utf-8')
new = open('D:/学习/0基础学Python/029一个任务/课后练习/new.txt', 'r', encoding= 'utf-8')
count = 0
differ = []

for line1 in old:
    line2 = new.readline()
    count += 1
    if line1 != line2:
        differ.append(count)

old.close()
new.close()


print('两个文件共有 %s 处不同' % len(differ))
for each in differ:
    print('第 %d 行不一样' % each)




