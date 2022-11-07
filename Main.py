import Path
from base import BaseStation
from bullshitmap import BullshitMap
import random
import time
from datetime import datetime
import drone
# random.seed(datetime.now())

# INIT OF THE MAP SIZE
# mapX = 30
# mapY = 18
stationX = 12
stationY = 6

mapX = 60
mapY = 36
drone_width_Of_View = 21
drone_battery = 200
number_of_drones = 1
drones = []

# =============================
# INIT OF THE DRONE AND LOST
# =============================
droneX = random.randrange(mapX-1)
droneY = random.randrange(mapY-1)
lostX = random.randrange(mapX-1)
lostY = random.randrange(mapY-1)

# FOR TESTING
# droneX = 6
# droneY = 6
# lostX = 12
# lostY = 3

areaStatus = [["not scouted" for y in range(mapY)] for x in range(mapX)] 
areaStatus[droneX][droneY] = "scouted"
areaStatus[lostX][lostY] = "bingo"

# simpleMap.initMap(mapX, mapY)
for i in range(0,number_of_drones):
    drone_pos_X = random.randrange(mapX)
    drone_pos_Y = random.randrange(mapY)
    areaStatus[drone_pos_X][drone_pos_Y] = "scouted"
    # simpleMap.init_drone(drone_pos_X, drone_pos_Y)
    added_drone = drone.Drone(i,drone_width_Of_View,drone_battery,drone_pos_X,drone_pos_Y,0,0,0,0)
    drones.append(added_drone)

# INIT THE BASE STATION
base = BaseStation( mapX, mapY, number_of_drones, drone_width_Of_View, stationX, stationY, lostX, lostY, drone_battery_capacity=50 )
dronePos = base.getPositionOfDrones()

# INIT OF THE MAP
simpleMap = BullshitMap()
simpleMap.initMap(mapX, mapY)
simpleMap.init_lost_person(lostX ,lostY)
simpleMap.init_station(stationX ,stationY)

simpleMap.init_drone(dronePos[0], dronePos[1])



areaStatus[lostX][lostY] = "bingo"
simpleMap.init_lost_person(lostX ,lostY)

######

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

tickCount = 0
survivorFound = False

while(survivorFound == False):
    
    dronePos = base.nextMove()
    simpleMap.update_drone_pos(dronePos[0], dronePos[1])
    simpleMap.mark_searched_area(dronePos[0], dronePos[1])
    # # print( (areaStatus[1]) )
    # droneX,droneY = randomPath(droneX,droneY)
    # # DroneX = DroneX+1
    # simpleMap.update_drone_pos(droneX,droneY)
    # if(areaStatus[droneX][droneY] == "bingo"):
    #     print("Survivor found in ", tickCount, " ticks!")
    #     survivorFound = True
    # else:
    #     simpleMap.mark_searched_area(droneX, droneY)
    #     areaStatus[droneX][droneY] = "scouted"
    #     tickCount += 1
    # print(f"drone:   {droneX}, {droneY}")
    for drone in drones:
        drone_pos = drone.get_position()
        drone_id = drone.get_id()
        droneX,droneY = randomPath(drone_pos[0],drone_pos[1])
        areaStatus[droneX][droneY] = "scouted"
        drone.set_position(droneX,droneY)
        simpleMap.update_drone_pos(droneX,droneY)
        if(areaStatus[droneX][droneY] == "bingo"):
            print("Survivor found in ", tickCount, " ticks!")
            survivorFound = True
        else:
            simpleMap.mark_searched_area(droneX, droneY)
    tickCount += 1

# time.sleep(5)

#for i in range(20):
    #dronePosition = PathScheduler.getPath(dronePosition[0], dronePosition[1])
    #Draw a drone on the map somehow


