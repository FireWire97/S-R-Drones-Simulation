import Path
from base import BaseStation
from bullshitmap import BullshitMap
import random
import time
from datetime import datetime

# random.seed(datetime.now())

# =============================
# INIT OF THE DRONE AND LOST
# =============================

# INIT OF THE MAP SIZE
mapX = 12
mapY = 8
# LOCATION OF THE STATION
stationX = 8
stationY = 4
# LOCATION OF THE LOST PERSON
lostX = 3
lostY = 3
# NUMBER OF DRONES
numberOfDrones = 1


# INIT THE BASE STATION
base = BaseStation(mapX, mapY, numberOfDrones, stationX, stationY, lostX, lostY, drone_battery_capacity=20)
dronePosistions = base.getPositionOfDrones()

# INIT OF THE MAP
simpleMap = BullshitMap()
simpleMap.initMap(mapX, mapY)
simpleMap.init_lost_person(lostX, lostY)
simpleMap.init_station(stationX, stationY)


# for index in range(numberOfDrones):
# simpleMap.init_drone(dronePosistions[0][0], dronePosistions[0][1], index)
simpleMap.init_drone(dronePosistions[0][0], dronePosistions[0][1], numberOfDrones)


tickCount = 0
survivorFound = False


while survivorFound == False:

    dronePosistions = base.nextMove()
    # dronePosistions = dronePosistions
    for idx, dronePos in enumerate(dronePosistions):
        simpleMap.update_drone_pos(dronePos[0], dronePos[1], idx)
        simpleMap.mark_searched_area(dronePos[0], dronePos[1])
    simpleMap.update_map()
