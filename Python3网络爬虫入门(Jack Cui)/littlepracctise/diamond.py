#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
for i in range(4):
    for line in range(3-i):
        print(' ',sep='',end='')
    for column in range(2*i+1):
        print('*',sep='',end='')
    print('')
for i in range(3):
    for line in range(i+1):
        print(' ',sep='',end='')
    for column in range(5-2*i):
        print('*',sep='',end='')
    print('')
'''
##菱形
s = '*'
for i in range(1, 8, 2):
    print((s*i).center(7))
for i in reversed(range(1, 6, 2)):
    print((s*i).center(7))

##等边三角
a = int(input("请输入等边三角形的边长："))
for i in range(1,2*a,2):
    print((s*i).center(2*a-1))

##序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和
from functools import reduce
a = 2
b = 1
Arr = []
num = int(input("请输入要计算的项数："))
for i in range(num):
    Arr.append(a / b)
    a , b = a + b , a
print(Arr)
print(reduce(lambda x,y:x+y,Arr))

##回数过滤
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

if __name__ == "__main__":
    n = int(input("您要查询前多少的回数？\n请您输入："))
    result = filter(is_palindrome,range(1,n+1))
    print(list(result))


