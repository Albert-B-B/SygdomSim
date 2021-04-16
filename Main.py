# -*- coding: utf-8 -*-
#Program simulates the spreading of a dissease

import tkinter as tk
from random import randrange

import sys
import time
import ParameterHandler as config

import random
import math
import matplotlib.pyplot as plt


#Initializes settings
args = sys.argv
config.initializeConfig(args)
#Parameters of canvas height and width
widthCanvas = config.getVal("-width")
heightCanvas = config.getVal("-height")

#Sets up tkinter canvas
root = tk.Tk()
canvas = tk.Canvas(root,height=heightCanvas,width=widthCanvas,background="grey")
canvas.pack()

#Tracks time
loop_factor = 0

#Arrays to store how many people are en each state at each iteration
dataHealthy = []
dataSick = []
dataDead = []
dataImune = []
dataTempImune = [] 

#Class representing one agent
class person:
    def __init__(self,status,x,y,color):
        #0 for non contaminated and 1 for infected.
        self.status = status
        
        #Coordinates of person in xy plane
        self.x = x
        self.y = y

        self.color = color
        self.TimeOfMovement = 0
        self.healthyTime = 0  #How much time person has left as temporarily imune
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

        if self.TimeOfMovement <= 0:
            self.Movex, self.Movey, self.TimeOfMovement = self.move()
        elif self.TimeOfMovement > 0:
            self.x += self.Movex * loop_factor
            self.y += self.Movey * loop_factor
            self.TimeOfMovement -= loop_factor
            self.x = self.x % widthCanvas
            self.y = self.y % heightCanvas
        else:
            print("Error: TimeOfMovement below threshold")
    #So you can print object interformation
    def __str__(self):
        return "Status: {} Position: {},{} Color: {}".format(self.status,self.x,self.y,self.color)
    def spread(self, folk):
        spreadType = config.getVal("-spreadType") #How it spreads from each person currently only one option
        spreadRadius = config.getVal("-spreadRadius") #How cole people need to be to spread dissease
        #Chances of changing into different state 1.
        deathChance = config.getVal("-chanceDeath")
        imunityChance = config.getVal("-chanceImune")
        healthyChance = config.getVal("-chanceHealthy")
        if self.status == 1:
            #Checks for every other person if they are so close as to spread disease to.
            for i in folk:
                if spreadType == 0:
                    if i.status == 0 and math.sqrt((self.x-i.x)**2+(self.y-i.y)**2) <= spreadRadius:
                        #Does makes it so it doesn't imeadieately spread from the person
                        i.status = -1
            #Checks for how a persons state changes
            if random.random() < deathChance*loop_factor:
                self.status = -2
                self.TimeOfMovement = 0
            elif random.random() < imunityChance*loop_factor:
                self.status = -3
            elif random.random() < healthyChance*loop_factor:
                self.status = 4
                self.color = "yellow"
                self.healthyTime = random.randint(config.getVal("-tempImuneMin"),config.getVal("-tempImuneMax"))
    #Handles the result of spreading
    def resolveSpread(self):
        #Makes people sick
        if self.status == -1:
            self.status = 1
            self.color = config.getVal("-sickColor")
        #Person died
        elif self.status == -2:
            self.status = 2
            self.color = config.getVal("-deathColor")
        #Person became permanantly imune
        elif self.status == -3:
            self.status = 3
            self.color = config.getVal("-imuneColor")
        #Person is temporarily imune and we remove some of the time left as temporary imunity
        elif self.status == 4:
            self.healthyTime -= 1*loop_factor
            if self.healthyTime <= 0:
                self.status = 0
                self.color = config.getVal("-healthyColor")
                
#Not yet added feuture 
class ManInBlack(person):
    pass

#Array that saves every person object
people = []
numPep = config.getVal("-pop") #Number of people
#Adds initial healthy people at random locations
for i in range(numPep):
    people.append(person(0,random.randint(0, widthCanvas),random.randint(0,heightCanvas),"blue"))
#Adds initial sick people in random locations
for i in range(config.getVal("-randInitialSick")):
    people.append(person(1,random.randint(0, widthCanvas),random.randint(0,heightCanvas),"blue"))

#Spreads disease troughout the entire population
def spreadPop():
    global people
    for i in people:
        i.spread(people)
    for i in people:
        i.resolveSpread()
        
#Saves how many people are at each state at time of calling
def recordData():
    global dataHealthy 
    global dataSick 
    global dataDead 
    global dataImune 
    global dataTempImune  
    statusCount = [0,0,0,0,0]
    for i in people:
        statusCount[i.status] += 1
    dataHealthy.append(statusCount[0])
    dataSick.append(statusCount[1])
    dataDead.append(statusCount[2])
    dataImune.append(statusCount[3])
    dataTempImune.append(statusCount[4])
    
#Shows a plot of the data about states
def showData():
    points = list(range(len(dataHealthy))) # Number of observations
    #Adds a curve for each state measured
    plt.plot(points,dataHealthy,"b",points,dataSick,"r",points,dataDead,"k",points,dataImune,"cyan",points,dataTempImune,"y")
    plt.savefig("graf.png")
    plt.show()
    

#Main loop
done = False #Tracks if main loop should end
while True:
    canvas.delete("all") #Clears canvas
    canvas.create_rectangle(0, 0, heightCanvas, widthCanvas, fill="grey") #draws a grey background
    start_time = time.time() #Saves time when iteration started

    #Draws each person but canvas is not updated
    for person in people:
        person.draw()

    #Updates canvas
    canvas.pack()
    root.update_idletasks()
    root.update()
    

    spreadPop() #Spreads dissease troughout population
    loop_factor = (time.time() - start_time) #Calculates how long calculations took
    recordData() #Saves the number of people in each state
    
    #Checks if program need to end
    if done:
        break
    #Checks if anyone is infected if no one is the program exists
    done = True
    for person in people:
        if person.status==1:
            done = False
            break
#counts the number of dead people
dead = 0
for i in people:
    if i.status == 2:
        dead += 1
showData() #Shows graph
print("Dead: " + str(dead)) # prints number of people
input("Time stop") #Input to stop program from exiting
root.destroy() #Closes window with tkinter canvas