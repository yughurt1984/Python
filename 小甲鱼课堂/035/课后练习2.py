#!/usr/bin/python
# coding:utf-8

import easygui as g
import os

msg_content = ''
file_name = g.fileopenbox(msg= msg_content,title= '显示文件内容', default= '*.txt')


try:
    msg_content = os.path.split(file_name)[1]
    with open(file_name, 'r',encoding= 'utf-8') as f:
        
        g.textbox(msg= '文件 %s 的内容如下:' % msg_content,title= '显示文件内容', text= f.read())
except OSError:
    g.msgbox(msg= '错误')