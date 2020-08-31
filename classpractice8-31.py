# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:50:36 2020

@author: Robert Richter
name of Program: in class practice 8-31
"""

numberOfStudents = int(input("Input whole number of students: "))
if numberOfStudents != 0:
    averageGrade = 0

    for i in range(0, numberOfStudents):
        studentGrade = int(input("Input grade (0-100) for student #"+str(i+1)+": "))
        averageGrade += studentGrade
        if studentGrade >=90:
            studentLetterGrade="A"
        elif studentGrade >=80:
            studentLetterGrade="B"
        elif studentGrade >=70:
            studentLetterGrade="C"
        elif studentGrade >=60:
            studentLetterGrade="D"
        else:
            studentLetterGrade="F"
        print("Student #",str(i+1),"'s grade is an", studentLetterGrade)
        i = i+1
    print("The average grade is ", averageGrade/numberOfStudents)
        
else: print("There are zero students")