# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 11:54:31 2021

@author: Owade
"""
def grading_system():
    subject=str(input("Enter the subject: "))
    score=int(input("Please enter your marks: "))  
    
      
    if score > 100 or score < 0:
        print ("Wrong score values. Please, try again!")
    elif score > 80:
        grade = "A"
    elif score > 70:
        grade = "B"
    elif score > 60:
        grade = "C"
    elif score > 50:
        grade = "D"
    elif score > 40:
        grade = "E"
    else:
        grade = "F"
    
    if score < 100 and score > 0:
        print("{} {} | {}".format(subject, score, grade))
        
grading_system()