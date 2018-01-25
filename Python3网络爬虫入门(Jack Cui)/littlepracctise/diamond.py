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
s = '*'
for i in range(1, 8, 2):
    print((s*i).center(7))
for i in reversed(range(1, 6, 2)):
    print((s*i).center(7))