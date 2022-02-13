#!/usr/bin/python
# coding:utf-8

while True:
    name = input("请输入用户名")
    psw = input("请输入密码")
    email = input('请输入邮箱')
    
    name = name[0:20]
    psw = psw[0:20]
    email = email[0:20]

    if name.lower() == "q" or psw.lower() == "q" or email.lower() == "q":
        print("不在输入了！") 
        break

print("用户名  密码   邮箱")
print("%s  %s  %s" % name,psw,)
