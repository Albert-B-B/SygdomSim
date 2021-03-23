# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 12:39:29 2021

@author: Mi
"""
#Contains standard values for settings.
defaultConfig = {
    "-width" : 500,
    "-height" : 500,
    "-pop" : 100,
    "-chanceDeath" : 0.001,
    "-chanceImune" : 0.0005,
    "-chanceHealthy" : 0.001,
    "-speed" : 30,
    "-squareLength" : 5,
    "-spreadRadius" : 20,
    "-tempImuneMin" : 300,
    "-tempImuneMax" : 750,
    "-spreadType" : 0,
    "-turnIntervalMin" : 10,
    "-turnIntervalMax" : 60,
    "-sickColor" : "red",
    "-healthyColor" : "blue",
    "-imuneColor" : "cyan",
    "-deathColor" : "black",
    "-tempImuneColor" : "yellow"
    }
#Has current values
config = defaultConfig.copy()


def initializeConfig(args):
    global config
    for i in range(1,len(args),2):
        try:
            if type(defaultConfig[args[i]]) == type(1):
                config[args[i]] = int(args[i+1])
            elif type(defaultConfig[args[i]]) == type(1.0):
                config[args[i]] = float(args[i+1])
            elif type(defaultConfig[args[i]]) == type("string"):
                config[args[i]] = str(args[i+1])
            elif type(defaultConfig[args[i]]) == type(True):
                config[args[i]] = bool(args[i+1])
        except TypeError:
            print("ERROR: Can not convert " + str(args[i+1]) + "to default type" )
        except:
            print("ERROR: " + str(args[i])+" is not a valid parameter")
    
def getVal(parameter):
    try:
        return config[parameter]
    except:
        print("ERROR: " + str(parameter) + " is not a valid parameter")
        
if __name__ == "__main__":
    import sys
    args = sys.argv
    print(args)
    initializeConfig(args)
    config["-width"] = 1
    print(config)