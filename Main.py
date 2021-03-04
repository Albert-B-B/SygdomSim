# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:23:44 2021

@author: 
"""
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root,height=400,width=400,background="grey")
canvas.pack()

PERSON_RADIUS = 10

class person:
    def __init__(self,status,position,color):
        #
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
        self.position[0] += 0.01
        self.position[1] += 0.01

N = 10
people = []
for i in range(10):
    people.append(person(0,[0,0],"black"))

#UI

while True:
    for person in people:
        person.draw()
        
        canvas.pack()
        root.update_idletasks()
        root.update()