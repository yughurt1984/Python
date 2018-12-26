#!/usr/bin/python
# coding:utf-8

import easygui as g
import os

msg_content = ''
file_name = g.fileopenbox(msg= msg_content,title= '显示文件内容', default= '*.txt')


def sav_file(file_name, text_name):
    f = open(file_name, 'w',encoding= 'utf-8')
    f.writelines(text_name)
    g.msgbox(msg= '保存成功！')
    f.close()


try:
    msg_content = os.path.split(file_name)[1]
    with open(file_name, 'r',encoding= 'utf-8') as f:
        old_text = f.read()
        new_text = g.textbox(msg= '文件 %s 的内容如下:' % msg_content,title= '显示文件内容', text= old_text)
except OSError:
    g.msgbox(msg= '错误')


while True:
    if old_text != new_text:
        choice = g.buttonbox(msg= '检测到文件内容发生改变，请选择以下操作', title= '警告', choices= ['覆盖保存', '放弃保存', '另存为'])
        break
if choice == '覆盖保存':
    sav_file(file_name, new_text)
elif choice == '另存为':
    file_name = g.filesavebox(msg= '请选择保存的文件夹', default= 'record', filetypes= '*.txt', title= '保存')
    sav_file(file_name,new_text)
else:
    g.msgbox(msg= '退出！')
            

