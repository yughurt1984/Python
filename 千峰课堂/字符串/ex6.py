#!/usr/bin/python
# coding:utf-8

word1 = 'They are students.'
word2 = "aeiou"
word3 = ''

'''
for i in word1:
    if i not in word2:
        word3 += i
print(word3)
'''
for i in word1:
    if i in word2:
        word1 = word1.replace(i,"")
print(word1)