#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:53:14 2019

@author: bdnooner
"""
def factor_int(number):
    factors = ""
    if number < 0:
        return "Invalid entry"
    elif number >= 0:
        if number == 0:
            return str(number)
        elif number > 0:
            divisor = 1
            while divisor <= number:
                if number % divisor == 0:
                    new_factor = int(number/divisor)
                    factors += str(new_factor) + " "
                divisor += 1
            return factors            
num = int(input("Input an integer to factor out:\t"))
print(factor_int(num))
