# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:23:44 2021

@author:
"""
import tkinter as tk
from random import randrange

import time

import random
import math


#Parameters of canvas height and width
widthCanvas = 400
heightCanvas = 400

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
    def move(self):
        Angle = randrange(0,360)
        TOM = randrange(1,6,1)
        SPEED = 1.6
        Movementx = random.randint(0,30)*math.cos(math.radians(Angle))
        Movementy = random.randint(0,30)*math.sin(math.radians(Angle))
        return Movementx, Movementy
    def draw(self):
        r = 5
        canvas.create_rectangle(self.x-r, self.y-r, self.x+r, self.y+r, fill=self.color)

        Movex, Movey = self.move()
        self.x += Movex * loop_factor
        self.y += Movey * loop_factor

    def __str__(self):
        return "Status: {} Position: {},{} Color: {}".format(self.status,self.x,self.y,self.color)
    def spread(self, folk):
        #How it spreads from each person
        spreadType = 0
        spreadRadius = 60
        deathChance = 0.002
        imunityChance = 0.001
        if self.status == 1:
            for i in folk:
                if spreadType == 0:
                    if i.status == 0 and math.sqrt((self.x-i.x)**2+(self.y-i.y)**2) <= spreadRadius:
                        #Does makes it so it doesn't imeadieately spread from the person
                        i.status = -1
            if random.random() < deathChance:
                self.status = -2
            elif random.random() < imunityChance:
                self.status = -3
    #Handles the result of spreading
    def resolveSpread(self):
        if self.status == -1:
            self.status = 1
            self.color = "red"
        elif self.status == -2:
            self.status = 2
            self.color = "Black"
        elif self.status == -3:
            self.status = 3
            self.color = "cyan"


people = []
#Number of people
numPep = 50
for i in range(numPep):
    people.append(person(0,random.randint(0, widthCanvas),random.randint(0,heightCanvas),"blue"))
people.append(person(1,300,300,"red"))
people.append(person(1,300,301,"red"))
#Spreads disease for entire population
def spreadPop():
    global people
    for i in people:
        i.spread(people)
    for i in people:
        i.resolveSpread()

#UI

while True:
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 500, 500, fill="grey")
    start_time = time.time()

    for person in people:
        person.draw()


    canvas.pack()
    root.update_idletasks()
    root.update()

    loop_factor = (time.time() - start_time)
    spreadPop()