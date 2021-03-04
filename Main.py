# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:23:44 2021

@author: 
"""
import tkinter as tk
import random 
root = tk.Tk()
canvas = tk.Canvas(root,height=400,width=400,background="grey")
canvas.pack()

PERSON_RADIUS = 10

class person:
    def __init__(self,status,position,color):
        #0 for non contaminated and 1 for infected.
        self.status = status
        #Format [x,y]
        self.position = position
        self.color = color
        self.grafisk_obj = self.id=canvas.create_oval(position[0] - PERSON_RADIUS,position[1] - PERSON_RADIUS,position[0] + PERSON_RADIUS,position[1] + PERSON_RADIUS, fill=color, outline='')
    def move(self):
        pass
    def spread(self):
        pass
    def draw(self):
        canvas.move(self.grafisk_obj, self.position[0], self.position[1])
        self.position[0] += 0.001
        self.position[1] += 0.001
    def __str__(self):
        return "Status: {} Position: {} Color: {}".format(self.status,self.position,self.color)
    def spread(self, folk):
        #How it spreads from each person
        spreadType = 0
        if self.status == 1:
            for i in folk:
                if i.status == 0:
                    #Does makes it so it doesn't imeadieately spread from the person
                    i.status = -1
    #Handles the result of spreading
    def resolveSpread(self):
        if self.status == -1:
            self.status = 1 
width = 500
height = 500
people = []
#Number of people
numPep = 2
for i in range(numPep):
    people.append(person(1,[0,0],"black"))
print(people[1])
people[0].spread(people)
print(people[1])

#UI

while False:
    for person in people:
        person.draw()
        
        canvas.pack()
        root.update_idletasks()
        root.update()