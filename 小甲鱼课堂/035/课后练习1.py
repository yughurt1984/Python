#!/usr/bin/python
# coding:utf-8

import easygui as g

title_name = '账号中心'
msg_name = '请填写一下信息！'

fields_name_list = ['*用户名','*真实姓名','固定电话','*手机号码','QQ','*Email']
values_content_list = []
values_content_list = g.multenterbox(msg= msg_name, title= title_name,fields= fields_name_list)


while True:
    msg_error_name = '' 
    for each_num in range(0,len(values_content_list)):
        msg_error_name += '【 %s 】 为必填项\n'  % fields_name_list[each_num]
        
        
    if values_content_list[each_num] == '' and fields_name_list[each_num][0] == '*':
        g.multenterbox(msg= msg_error_name, title= title_name,fields= fields_name_list,values= values_content_list)
        break
            
           
        
