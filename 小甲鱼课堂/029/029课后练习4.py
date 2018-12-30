#!usr/bin/env python
# -*- coding:utf-8 _*-


file_name = input('请输入要打开的文件：')
change_old = input('请输入需要替换的字符：')
change_new = input('请输入新的字符：')
f = open('D:/学习/0基础学Python/029一个任务/课后练习/' + file_name, 'r', encoding='utf-8')
content = f.read()

count_num = content.count(change_old)
print('文件 %s 中共有 %s 个 %s' % (file_name, count_num, change_old))
f.close()

confirm = input('【Yes or No】')
if confirm == 'Yes':
    f = open('D:/学习/0基础学Python/029一个任务/课后练习/' + file_name, 'w', encoding='utf-8')
    content = content.replace(change_old, change_new)
    f.write(content)
f.close





