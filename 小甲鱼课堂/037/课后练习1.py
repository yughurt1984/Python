#!/usr/bin/python
# coding:utf-8

import random
import easygui as g

time = 0
direction = ([-1,0], [0,-1], [1,0], [0,1])


class Turtle:
    def __init__(self, positionX, positionY, life):
        self._posionX = positionX
        self._posionY = positionY
        self._posion = [self._posionX, self._posionY]
        self._life = life
        if self._life == 0:
            g.msgbox('游戏结束，乌龟饿死了！')
    
    def move(self):
        moveDirection = random.choice(direction)        #随机一个方向
        moveTimes = random.randint(1,3)                 #随机（1,2）次数
        moveNum = 0
        while moveNum != moveTimes:
            if 0 < self._posionX < 10 or 0 < self._posionY < 10:        #判断边际
                self._posion = self._posion + moveDirection             #移动位置
                moveNum += 1
            else:
                continue  
    
    def getLife(self):
        return self._life

    def getPosion(self):  
        return self._posion
        
       

#class Fish:
   

