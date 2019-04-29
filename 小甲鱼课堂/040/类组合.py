#!/usr/bin/python
# coding:utf-8

class Fish:
    def __init__(self, x):
        self.num = x

class Turtle:
    def __init__(self, x):
        self.num = x

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("水池里共有 %d 只乌龟， %d 条鱼" % (self.turtle.num, self.fish.num))
        