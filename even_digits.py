#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:37:19 2019
This function will print all even numbers within the range of 0-100 (inclusive)

@author: bdnooner
"""
num = 0
while num < 101:
    if num % 2 == 0:
        print(num)
    num += 1

for num in range(0, 101, 2):
    print (num)
