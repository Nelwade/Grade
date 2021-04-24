# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 17:27:37 2021

@author: Owade
"""

my_dict={}

def grade_input():
    
    subject=input("Please enter the subject: ")
    score=int(input("Please enter the score: "))
    while score > 100 or score < 0:
        print ("Wrong score values. Please, try again!")
        subject=input("Please enter the subject: ")
        score=int(input("Please enter the score: "))
    my_dict[subject]=score

def grading_system():
    if score > 80:
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
            

grade_input() #First subject
grade_input() #second subject
grade_input() #third subject
grade_input() #fourth subject
grade_input()

#print(my_dict)

for subject, score in my_dict.items():
    grading_system()
    
total_score=0
for score in my_dict.values():
    total_score+=score
print("Total Score is: ", total_score)

average_score=total_score/len(my_dict)

if average_score > 80:
            grade = "A"
elif average_score > 70:
            grade = "B"
elif average_score > 60:
            grade = "C"
elif average_score > 50:
            grade = "D"
elif average_score > 40:
            grade = "E"
else:
            grade = "F"
    

print("Average grade: ", grade)
