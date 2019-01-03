#!/usr/bin/python
# coding:utf-8

import random
import easygui as g
import numpy

time = 0
direction = ([-1,0], [0,-1], [1,0], [0,1])


class Turtle:
    def __init__(self, turtleLife):
        self._turtlePosion = numpy.array([0, 0])
        self._turtleLife = turtleLife
    
    def move(self):
        self._life -= 1
        moveDirection = numpy.array(random.choice(direction))        #随机一个方向
        moveTimes = random.randint(1,3)                 #随机（1,2）次数
        moveNum = 0
        while moveNum != moveTimes:
            if 0 < self._turtlePosion[0] < 10 or 0 < self._turtlePosion[1] < 10:        #判断边际
                self._turtlePosion = self._turtlePosion + moveDirection self._turtlePosion = self._posion + moveDirection             #移动位置
                moveNum += 1
            else:
                continue
        
    
    def getLife(self):
        return self._life

    def getPosion(self):  
        return self._posion
        
       

class Fish:
    def __init__(self, fishNum):
        self._posionX = positionX
        self._posionY = positionY
        self._posion = [self._posionX, self._posionY]
        self._life = life
    
    def move(self):
        self._life -= 1
        moveDirection = numpy.array(random.choice(direction))        #随机一个方向
        moveTimes = random.randint(1,3)                         #随机（1,2）次数
        moveNum = 0
        while moveNum != moveTimes:
            if 0 < self._turtlePosion[0] < 10 or 0 < self._turtlePosion[1] < 10:        #判断边际
                self._turtlePosion = self._turtlePosion + moveDirection self._turtlePosion = self._posion + moveDirection             #移动位置
                moveNum += 1
            else:
                continue

while self._life != 0 or self._fishMum != 0:

