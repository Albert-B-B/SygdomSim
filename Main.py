# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:23:44 2021

@author: 
"""
import tkinter as tk

class person:
    def __init__(self,status,position,color):
        #0 for non contaminated and 1 for infected.
        self.status = status
        #Format [x,y]
        self.position = position
        self.color = color
    def __str__(self):
        return "Status: {} Position: {} Color: {}".format(self.status,self.position,self.color)
    def move(self):
        pass
    def spread(self, folk):
        #How it spreads from each person
        spreadType = 0
        if self.status == 1:
            for i in folk:
                if i.status == 1:
                    i.status = 0
people = []
#Number of people
numPep = 2
for i in range(numPep):
    people.append(person(1,[0,0],"black"))
print(people[1])
people[0].spread(people)
print(people[1])
#UI
        

        