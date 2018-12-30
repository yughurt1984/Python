#!usr/bin/env python
# -*- coding:utf-8 _*-

file_name = str(input('请输入文件名：'))

f = open('D:/学习/0基础学Python/029一个任务/课后练习/' + file_name, 'w')
while True:
    file_content = input('请输入内容：')
    if file_content != ':w':
        f.write('%s\n' % file_content)
    else:
        print('终止输入！')
        break

f.close()

