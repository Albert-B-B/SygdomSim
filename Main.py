# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:23:44 2021

@author: 
"""
import tkinter as tk
from random import randrange
import math

class person:
    def __init__(self,status,position,color):
        #
        self.status = status
        #Format [x,y]
        self.position = position
        self.color = color
    def move(self):
        Angle = randrange(0,360)
        TOM = randrange(1,6,1)
        SPEED = 1.6
        self.Movementx = math.cos(math.radians(Angle)) 
        self.Movementy= math.sin(math.radians(Angle))
    def spread(self):
        pass

people = []
for i in range(n):
    people.append(person(0,[0,0],"black"))

#UI
        

        