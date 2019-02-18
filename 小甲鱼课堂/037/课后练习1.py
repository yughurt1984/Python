#!/usr/bin/python
# coding:utf-8

import random
import easygui as g


positionScope = [0,10]



class Turtle:
    def __init__(self):
        self.power = 100
        self.turtlePosion = random.randint(positionScope[0], positionScope[1])
        self._turtleLife = turtleLife
    
    def turtleMove(self):
        self._turtleLife -= 1
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
    def __init__(self, fishNum):        #创建10条鱼的初始坐标
        self._fishNum = fishNum
        self._fishPosition_dict = {}
        for i in range(0,int(self._fishNum)):
            fishPositionX = random.randint(0,10)
            fishPositionY = random.randint(0,10)
            fishPosition = [fishPositionX, fishPositionY]
            self._fishPosition_dict[i] = fishPosition

    
    def fishMove(self):
        fishMoveDirection = random.choice(direction)       #随机一个方向
        for key in self._fishPosition_dict.keys():      #10条鱼一起动
            if 0 < self._fishPosition_dict[key][0] < 10 or 0 < self._fishPosition_dict[key][0][1] < 10:        #判断边际
                while True:
                    self._fishPosition_dict[key] = [self._fishPosition_dict[key][0] + fishMoveDirection[0], self._fishPosition_dict[key][1] + fishMoveDirection[1]]
                    break
                else:
                    continue

    def getFishNum(self):
        return self._fishNum

    def getFishPosion(self):  
        return self._fishPosition_dict.items()

    def delFish(self):
        


turtle = Turtle(100)
fish = Fish(10)

while turtle.getTurtleLife != 0 or len(Fish.getFishPosion) != 0:
    turtle.turtleMove()
    fish.fishMove()
    fishPosition = fish.getFishPosion()
    turtlePosition = turtle.
    if turtle.getTurtlePosion in 

