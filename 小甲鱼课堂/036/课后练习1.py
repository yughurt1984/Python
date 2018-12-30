#!/usr/bin/python
# coding:utf-8

class Rectangle:
    lenth = float(5)
    wild = float(4)
    
    
    def getRect(self):
        print('这个矩形的长是：%.2f ,宽是 %.2f' % (self.lenth, self.wild))

    def setRect(self):
        print('请输入矩形的长和宽...')
        self.lenth = float(input('长：'))
        self.wild = float(input('宽：'))

    def getArea(self):
        area = self.wild * self.lenth
        print('面积： %s' % area)



        
    
