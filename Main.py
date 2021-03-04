# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:23:44 2021

@author: 
"""
import tkinter as tk

import time


import random 
import math

root = tk.Tk()
canvas = tk.Canvas(root,height=400,width=400,background="grey")
canvas.pack()

PERSON_RADIUS = 10
loop_factor = 0

class person:
    def __init__(self,status,x,y,color):
        #0 for non contaminated and 1 for infected.
        self.status = status
        #Format [x,y]
        self.x = x
        self.y = y
        self.color = color
        self.grafisk_obj = self.id=canvas.create_oval(self.x - PERSON_RADIUS,self.y - PERSON_RADIUS,self.x + PERSON_RADIUS,self.y + PERSON_RADIUS, fill=color, outline='')
    def move(self):
        pass
    def draw(self):
        canvas.move(self.grafisk_obj, self.position[0], self.position[1])

        self.x += 1 * loop_factor
        self.y += 1 * loop_factor

    def __str__(self):
        return "Status: {} Position: {},{} Color: {}".format(self.status,self.x,self.y,self.color)
    def spread(self, folk):
        #How it spreads from each person
        spreadType = 0
        spreadRadius = 3
        if self.status == 1:
            for i in folk:
                if spreadType == 0:
                    if i.status == 0 and math.sqrt((self.x-i.x)**2+(self.y-i.y)**2) <= spreadRadius:
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
numPep = 10
for i in range(numPep):
    people.append(person(1,random.randint(0, width),random.randint(0,height),"black"))
print(people[1])
people[0].spread(people)
print(people[1])
def spreadPop():
    global people
    for i in people:
        i.spread()
    for i in people:
        i.resolveSpread()
#UI


while True:
    start_time = time.time()
    
    for person in people:
        person.draw()
        
    
    canvas.pack()
    root.update_idletasks()
    root.update()
    
    loop_factor = (time.time() - start_time)
