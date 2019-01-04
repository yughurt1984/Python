#!/usr/bin/python
# coding:utf-8

import random
import easygui as g


time = 0
direction = ([-1,0], [0,-1], [1,0], [0,1])


class Turtle:
    def __init__(self, turtleLife):
        self._turtlePosion = [0, 0]
        self._turtleLife = turtleLife
    
    def move(self):
        self._life -= 1
        turtleMoveDirection = random.choice(direction)       #随机一个方向
        turtleMoveTimes = random.randint(1,3)                 #随机（1,2）次数
        turtleMoveNum = 0
        while turtleMoveNum != turtleMoveTimes:
            if 0 < self._turtlePosion[0] < 10 or 0 < self._turtlePosion[1] < 10:        #判断边际
                self._turtlePosion= [self._turtlePosion[0] + turtleMoveDirection[0], self._turtlePosion[1] + turtleMoveDirection[1]]     #移动位置       
                turtleMoveNum += 1
            else:
                continue  
    
    def getTurtleLife(self):
        return self._turtleLife

    def getTurtlePosion(self):  
        return self._turtlePosion
        
       

class Fish:
    def __init__(self, fishNum):
        self._fishNum = fishNum
    
    def move(self):
        for i in range(0,self.fishNum):
            self._fishPosionX = random.randint(0,10)
            self._fishPosionY = random.randint(0,10)
            self._fishPosion = [self._fishPosionX, self._fishPosionY]
            self._fishPositon_list.append((i, self._fishPosion))
        
        fishMoveDirection = random.choice(direction)       #随机一个方向
        for j in range(0, len(self._fishPositon_list)):      #10条鱼一起动
            while fishMoveNum != fishMoveTimes:
                if 0 < self._fishPositon_list[j][1][0] < 10 or 0 < self._fishPosion[j][1][1] < 10:        #判断边际
                    self._fishPosion = [self._fishPositon_list[j][1][0] + fishMoveDirection[0], self._fishPositon_list[j][1][1] + fishMoveDirection[1]]
                else:
                    continue

    def getFishLife(self):
        return self._fishLife

    def getFishPosion(self):  
        return self._fishPosion_list


turtle = Turtle(100)
fish = Fish(10)

while self._turtleLife != 0 or self._fishMum != 0:


