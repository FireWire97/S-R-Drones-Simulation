import Path
from base import BaseStation
from pyplotmap import PyplotMap
import random
import time
from datetime import datetime
import drone

# SIMULATION PARAMETERS
numberOfSimulations = 5
visualisationOn = True

# MAP CONSTANTS
stationX = 12
stationY = 6

mapX = 60
mapY = 36
drone_width_Of_View = 21
drone_battery = 200
number_of_drones = 3
drones = []

# =============================
# INIT OF THE DRONE AND LOST
# =============================
# droneX = random.randrange(mapX-1)
# droneY = random.randrange(mapY-1)
# lostX = random.randrange(mapX-1)
# lostY = random.randrange(mapY-1)
lostX = 14
lostY = 6

areaStatus = [["not scouted" for y in range(mapY)] for x in range(mapX)] 
# areaStatus[droneX][droneY] = "scouted"
areaStatus[lostX][lostY] = "bingo"

# INIT THE BASE STATION
base = BaseStation( mapX, mapY, number_of_drones, drone_width_Of_View, stationX, stationY, lostX, lostY, drone_battery_capacity=50 )
# dronePos = base.getPositionOfDrones()

# INIT OF THE MAP
simpleMap = PyplotMap()
simpleMap.initMap(mapX, mapY)
simpleMap.init_lost_person(lostX ,lostY)
simpleMap.init_station(stationX ,stationY)

# simpleMap.initMap(mapX, mapY)
for i in range(0,number_of_drones):
    drone_pos_X = stationX
    drone_pos_Y = stationY
    # drone_pos_X = random.randrange(mapX)
    # drone_pos_Y = random.randrange(mapY)
    areaStatus[drone_pos_X][drone_pos_Y] = "scouted"
    simpleMap.init_drone(drone_pos_X, drone_pos_Y)
    added_drone = drone.Drone(i,drone_width_Of_View,drone_battery,drone_pos_X,drone_pos_Y,0,0,0,0)
    drones.append(added_drone)

def resetMap(self):
    areaStatus = [["not scouted" for y in range(mapY)] for x in range(mapX)] 
    return areaStatus

def randomPath(x,y):
    nextMoveValid = False
    i = 0
    while(nextMoveValid == False):
        decision = random.randint(0,3)
        #go up
        if(decision == 0):
            if(y < mapY-1):
                if(areaStatus[x][y+1] != "scouted" or i > 10):
                    return x,y+1
                else:
                    i += 1
        #go right
        elif(decision == 1):
            if(x < mapX-1):
                if(areaStatus[x+1][y] != "scouted" or i > 10):
                    return x+1,y
                else:
                    i += 1
        #go down
        elif(decision == 2):
            if(y > 0):
                if(areaStatus[x][y-1] != "scouted" or i > 10):
                    return x,y-1
                else:
                    i += 1
        #go left
        elif(decision == 3):
            if(x > 0):
                if(areaStatus[x-1][y] != "scouted" or i > 10):
                    return x-1,y
                else:
                    i += 1

luckySurvivors = 0
tickAvg = 0

for i in range(numberOfSimulations):
    
    tickCount = 0
    survivorFound = False

    while(survivorFound == False):
        
        # dronePos = base.nextMove()
        # simpleMap.update_drone_pos(dronePos[0], dronePos[1])
        # simpleMap.mark_searched_area(dronePos[0], dronePos[1])
        for drone in drones:
            drone_pos = drone.get_position()
            drone_id = drone.get_id()
            droneX,droneY = randomPath(drone_pos[0],drone_pos[1])
            drone.set_position(droneX,droneY)
            if(areaStatus[droneX][droneY] == "bingo"):
                print("Survivor found in ", tickCount, " ticks!")
                luckySurvivors += 1
                tickAvg += tickCount
                reaStatus = [["not scouted" for y in range(mapY)] for x in range(mapX)]
                for drone in drones:
                     drone_pos = [stationX, stationY]
                areaStatus[lostX][lostY] = "bingo"
                survivorFound = True
            else:
                areaStatus[droneX][droneY] = "scouted"
                simpleMap.mark_searched_area(droneX, droneY)
                
            simpleMap.update_drone_pos(droneX,droneY)
        tickCount += 1
        
        if(tickCount > 100):
            survivorFound = True
            tickAvg += tickCount
        
print("Simulation finished!")
print("After running ", numberOfSimulations, " simulations")
print("Using ", number_of_drones, " drones")
print(luckySurvivors ," out of ", numberOfSimulations, " survivors were found")
print("On average, it took ", tickAvg/numberOfSimulations, " ticks to find the survivor")

# time.sleep(5)

#for i in range(20):
    #dronePosition = PathScheduler.getPath(dronePosition[0], dronePosition[1])
    #Draw a drone on the map somehow


