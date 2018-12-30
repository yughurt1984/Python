#!usr/bin/env python
# -*- coding:utf-8 _*-


file_name = input('请输入要打开的文件：')
line_num = input('请输入需要显示前几行：')

file = open('D:/学习/0基础学Python/029一个任务/课后练习/'+ file_name,'r', encoding= 'utf-8')
print('文件 s% 的前 s% 行的内容如下：' % (file_name,line_num))
for line in range(int(line_num)):
    print(file.readline(), end= "")
file.close()
