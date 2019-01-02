#!/usr/bin/python
# coding:utf-8

class Ticket:
    def __init__(self, num, weekend = False, child = False):
        self.basic_price = 100
        self.num = num
        if weekend == True:
            self.weekend_price = 1.2
        else:
            self.weekend_price = 1
        if child == True:
            self.child_price = 0.5
        else:
            self.child_price = 1


    def calPrice(self):
        return self.num * self.basic_price * self.weekend_price * self.child_price
        
adult = Ticket(2)
child = Ticket(1, child = True)

print('总共票价为：%.1f' % (adult.calPrice() + child.calPrice()))
