#!/usr/bin/python
# coding:utf-8

boy = []
girl = []
count = 1

def save_file(boy, girl, count):
	file_name_boy = "boy_" + str(count) + ".txt"
	file_name_girl = "girl_" + str(count) + ".txt"

	boy_file = open(file_name_boy, 'w')
	girl_file = open(file_name_girl, 'w')
	boy_file.writelines(boy)
	girl_file.writelines(girl)

	boy_file.close()
	girl_file.close()


f = open('D:/学习/0基础学Python/029一个任务/课堂练习/record1.txt', encoding = "utf-8")
for each_line in f:
	if each_line[:5] != '=====':
		(role, line_spoken) = each_line.split(":", 1)
		if role == "小甲鱼":
			boy.append(line_spoken)
		if role == "小客服":
			girl.append(line_spoken)
	else:
		save_file(girl,boy,count)

		boy = []
		girl = []
		count += 1

save_file(boy,girl,count)
f.close()