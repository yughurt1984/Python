#!usr/bin/env python
# -*- coding:utf-8 _*-


def num(file_name, line_num):
    (num_begin, num_end) = line_num.split(':', 1)
    if num_begin == '':
        num_begin = 1
    elif num_end == '':
        num_end = -1

    if num_begin == 1 and num_end == -1:
        print_name = '的全文'
    elif num_begin == 1:
        print_name = '从开始到第 %s 行' % num_end
    elif num_end == -1:
        print_name = '从第 %s 行到末尾' % num_begin
    else:
        print_name = '从第 %s 行到第 %s 行' % (num_begin, num_end)
    print('文件 %s %s 的内容如下：' % (file_name, print_name))

    begin = int(num_begin) - 1
    end = int(num_end)
    line = end - begin

    f = open('D:/学习/0基础学Python/029一个任务/课后练习/' + file_name, 'r', encoding='utf-8')
    for i in range(begin):
        f.readline()

    if line < 0:
        print(f.read())
    else:
        for i in range(begin, end):
            print(f.readline(), end="")
    f.close()


file_name = input('请输入要打开的文件：')
line_num = input('请输入需要显示前几行：(格式如 3:5)')
num(file_name,line_num)





