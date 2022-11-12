from numpy import arange
import Path
from base import BaseStation
from pyplotmap import PyplotMap
import random
import time
import math
import numpy as np
from datetime import datetime

# random.seed(datetime.now())


# ==================================
# INIT OF THE SIMULATOR
# ==================================


results = []
nuberOfSimulations = 50
isSimulationShown = False
isRandomLocation = True


# ==================================
# INIT OF THE DRONE AND LOST PERSON
# ==================================

# INIT OF THE MAP SIZE
mapX = 60
mapY = 36
# LOCATION OF THE STATION
stationX = 22
stationY = 14
# LOCATION OF THE LOST PERSON
lostX = 3
lostY = 11
# NUMBER OF DRONES
numberOfDrones = 5
batteryCapacity = 400


for i in range(nuberOfSimulations):

    tickCount = 1
    if isRandomLocation:
        lostX = random.randint(0, mapX - 1)
        lostY = random.randint(0, mapY - 1)

    try:
        # INIT THE BASE STATION
        base = BaseStation(mapX, mapY, numberOfDrones, stationX, stationY, lostX, lostY, drone_battery_capacity=batteryCapacity)
        dronePosistions = base.getPositionOfDrones()

        # INIT OF THE MAP
        simpleMap = PyplotMap()
        simpleMap.initMap(mapX, mapY)
        simpleMap.init_lost_person(lostX, lostY)
        simpleMap.init_station(stationX, stationY)

        # for index in range(numberOfDrones):
        # simpleMap.init_drone(dronePosistions[0][0], dronePosistions[0][1], index)
        simpleMap.init_drone(dronePosistions[0][0], dronePosistions[0][1], numberOfDrones)

        # survivorFound = False

        while True:

            dronePosistions = base.moveOneTime()

            if isSimulationShown:
                for idx, dronePos in enumerate(dronePosistions):
                    simpleMap.update_drone_pos(dronePos[0], dronePos[1], idx)
                    simpleMap.mark_searched_area(dronePos[0], dronePos[1])
                simpleMap.update_map()
            tickCount += 1

    except:
        results.append(tickCount)

print(results)
