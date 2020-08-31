# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:41:53 2020

@author: Robert Richter
program: Module 2: Lab Assignment (Bonus)
"""

num1 = float(input("Input First Number: "))
num2 = float(input("Input Second Number: "))
num3 = float(input("Input Third Number: "))

smallnum = num1
middlenum = 0
largenum = 0

if num1 < smallnum:
    smallnum = num1
if num2 < smallnum:
    smallnum = num2
if num3 < smallnum:
    smallnum = num3
if num1 > largenum:
    largenum = num1
if num2 > largenum:
    largenum = num2
if num3 > largenum:
    largenum = num3
if num1 != largenum and num1 != smallnum:
    middlenum = num1
elif num2 != largenum and num2 != smallnum:
    middlenum = num2
elif num3 != largenum and num3 != smallnum:
    middlenum = num3
print("The numbers in ascending order are: ",smallnum,", ",middlenum,", ",largenum)
print("The smallest number is ",smallnum,", the middle number is ",middlenum,", and the largest number is ",largenum)