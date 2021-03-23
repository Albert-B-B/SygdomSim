# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:23:44 2021

@author:
"""
import tkinter as tk
from random import randrange

import sys
import time
import ParameterHandler as config

import random
import math

#Initializes settings
args = sys.argv
config.initializeConfig(args)
#Parameters of canvas height and width
widthCanvas = config.getVal("-width")
heightCanvas = config.getVal("-height")

root = tk.Tk()
canvas = tk.Canvas(root,height=heightCanvas,width=widthCanvas,background="grey")
canvas.pack()

loop_factor = 0

class person:
    def __init__(self,status,x,y,color):
        #0 for non contaminated and 1 for infected.
        self.status = status
        #Format [x,y]
        self.x = x
        self.y = y
        self.color = color
        self.TimeOfMovement = 0
        self.healthyTime = 0
    def move(self):
        #Controls direction and length in frames
        Angle = randrange(0,360)
        TOM = randrange(config.getVal("-turnIntervalMin"),config.getVal("-turnIntervalMax"),1)
        SPEED = config.getVal("-speed")
        Movementx = math.cos(math.radians(Angle))*SPEED
        Movementy = math.sin(math.radians(Angle))*SPEED
        if self.status == 2:
            Movementx = 0
            Movementy = 0
        return Movementx, Movementy, TOM

    def draw(self):
        r = config.getVal("-squareLength")
        canvas.create_rectangle(self.x-r, self.y-r, self.x+r, self.y+r, fill=self.color)

        if self.TimeOfMovement == 0:
            self.Movex, self.Movey, self.TimeOfMovement = self.move()
        elif self.TimeOfMovement > 0:
            self.x += self.Movex * loop_factor
            self.y += self.Movey * loop_factor
            self.TimeOfMovement -= 1
        else:
            print("Error: TimeOfMovement below threshold")

    def __str__(self):
        return "Status: {} Position: {},{} Color: {}".format(self.status,self.x,self.y,self.color)
    def spread(self, folk):
        #How it spreads from each person
        spreadType = config.getVal("-spreadType")
        spreadRadius = config.getVal("-spreadRadius")
        deathChance = config.getVal("-chanceDeath")
        imunityChance = config.getVal("-chanceImune")
        healthyChance = config.getVal("-chanceHealthy")
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
            elif random.random() < healthyChance:
                self.status = -4
                self.color = "yellow"
                self.healthyTime = random.randint(config.getVal("-tempImuneMin"),config.getVal("-tempImuneMax"))
    #Handles the result of spreading
    def resolveSpread(self):
        if self.status == -1:
            self.status = 1
            self.color = config.getVal("-sickColor")
        elif self.status == -2:
            self.status = 2
            self.color = config.getVal("-deathColor")
        elif self.status == -3:
            self.status = 3
            self.color = config.getVal("-imuneColor")
        elif self.status == -4:
            self.healthyTime -= 1
            if self.healthyTime == 0:
                self.status = 0
                self.color = config.getVal("-healthyColor")


people = []
#Number of people
numPep = config.getVal("-pop")
for i in range(numPep):
    people.append(person(0,random.randint(0, widthCanvas),random.randint(0,heightCanvas),"blue"))
people.append(person(1,350,350,"red"))
people.append(person(1,50,50,"red"))
#Spreads disease for entire population
def spreadPop():
    global people
    for i in people:
        i.spread(people)
    for i in people:
        i.resolveSpread()

#UI
done = False
while True:
    canvas.delete("all")
    canvas.create_rectangle(0, 0, heightCanvas, widthCanvas, fill="grey")
    start_time = time.time()

    for person in people:
        person.draw()


    canvas.pack()
    root.update_idletasks()
    root.update()

    loop_factor = (time.time() - start_time)
    spreadPop()
    if done:
        break
    done = True
    for person in people:
        if person.status==1:
            done = False
            break
dead = 0
for i in people:
    if i.status == 2:
        dead += 1
print("Dead: " + str(dead))
input("Time stop")
