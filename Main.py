import Path
from base import BaseStation
from bullshitmap import BullshitMap
import random
import time
from datetime import datetime
# random.seed(datetime.now())


# INIT OF THE MAP SIZE
mapX = 30
mapY = 18
stationX = 12
stationY = 6


# =============================
# INIT OF THE DRONE AND LOST
# =============================
# DroneX = random.randrange(mapX-1)
# DroneY = random.randrange(mapY-1)
# LostX = random.randrange(mapX-1)
# LostY = random.randrange(mapY-1)

# FOR TESTING
droneX = 6
droneY = 6
lostX = 12
lostY = 3

areaStatus = [["not scouted" for y in range(mapY)] for x in range(mapX)] 
areaStatus[droneX][droneY] = "scouted"
areaStatus[lostX][lostY] = "bingo"

# INIT THE BASE STATION
base = BaseStation( mapX, mapY, 1, stationX, stationY, lostX, lostY, drone_battery_capacity=50 )
dronePos = base.getPositionOfDrones()

# INIT OF THE MAP
simpleMap = BullshitMap()
simpleMap.initMap(mapX, mapY)
simpleMap.init_lost_person(lostX ,lostY)
simpleMap.init_station(stationX ,stationY)

simpleMap.init_drone(dronePos[0], dronePos[1])


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

