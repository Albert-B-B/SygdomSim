# Sickness Simulator
![SygdomSim](https://socialify.git.ci/Albert-B-B/SygdomSim/image?font=Source%20Code%20Pro&issues=1&language=1&owner=1&pattern=Circuit%20Board&theme=Dark)
This application was made to simulate how sickness spreads by proximity. 

![](preview.gif)

![](graf.png)

## Agent Types
Here are all of the different agent types.

### Healthy
Completely normal person with no immunity. These are the blue ones.

### Infected
A person who carries the disease. These are the red ones.

### Immune
Has developed immunity after being infected. These are the cyan ones.

### Temporarily Immune
Is temporarily immune to prevent being infected just after healing. These are the yellow ones.

### Dead
Has died. These are the black ones.

## Parameters
Here is a list of all the parameters and a description of them.

### -width
Decides the width of the canvas. Default value is 500.

### -height
Decides the height of the canvas. Default value is 500.

### -pop
Decides how many agents should be made. Default is 100.

### -chanceDeath
Decides how likely it is for an infected person to die. Default value is 0.01.

### -chanceImmune
Decides how likely it is for an infected person to become immune. Default value is 0.05.

### -chanceHealthy
Decides how likely it is for an infected person to become healthy. Default value is 0.1.

### -speed
Decides how far an agent moves each frame. Default value is 30.

### -squareLength
Decides how big the agent is. Default value is 5.

### -spreadRadius
Decides how far an infected agent can infect

### -tempImmuneMin
Decides minimum time that a agent can be temporarily imune. Default value is 0.

### -tempImmuneMax
Decides maximum time that a agent can be temporarily imune. Default value is 5.

### -spreadType
Decides how the disease is spread currently only distance is supported. Default value is 0.

### -turnIntervalMin
Decides minimum time in seconds it can take for an agent to change direction. Default value is 15.

### -turnIntervalMax
Decides maximum time in seconds it can take for an agent to change direction. Default value is 15.

### -healthyColor
Decides what color sick agents are. Default value is "red".

### -healthyColor
Decides what color healthy agents are. Default value is "blue".

### -immuneColor
Decides what color permanently immune agents are. Default value is "cyan".

### -deathColor
Decides what color dead agents are. Default value is "black"

### -tempImmuneColor
Decides what color temporarily immune agents are. Default value is "yellow".

### -randInitialSick
Decides how many sick people are initialy added. They are added at random locations. They are added to the total number of people. Default value is 2. 
