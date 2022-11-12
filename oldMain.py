from numpy import arange
import Path
from base import BaseStation
from pyplotmap import PyplotMap
import random
import time
import math
import numpy as np
from datetime import datetime
import drone
from math import sin, cos, sqrt, atan2


def coordinationOfPath():
    PointsOnPathData = [
        (0.15, 0.31),
        (0.15, 5.60),
        (2.26, 5.60),
        (1.62, 8.81),
        (2.39, 9.91),
        (3.10, 10.25),
        (4, 11.19),
        (4.06, 13.12),
        (3.61, 14.02),
        (5.54, 14.92),
        (7.26, 15.82),
        (8.05, 16.66),
        (9.16, 16.99),
        (9.85, 18.27),
        (11.00, 17.82),
        (13.45, 19.04),
        (13.58, 18.01),
        (12.81, 16.4),
        (13.77, 15.18),
        (14.54, 13.83),
        (14.93, 11.83),
        (18.02, 12.48),
        (19.69, 13.25),
        (21.23, 13.51),
        (22.00, 13.19),
        (23.51, 12.88),
        (24.51, 12.00),
        (26.12, 13.96),
        (27.34, 16.14),
        (28.11, 18.01),
    ]

    return PointsOnPathData


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

VisitedPointsOnPath = []
x_coordiateDiff = 0
Y_coordiateDiff = 0

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
base = BaseStation(mapX, mapY, number_of_drones, drone_width_Of_View, stationX, stationY, lostX, lostY, drone_battery_capacity=50)
# dronePos = base.getPositionOfDrones()

# INIT OF THE MAP
simpleMap = PyplotMap()
simpleMap.initMap(mapX, mapY)
simpleMap.init_lost_person(lostX, lostY)
simpleMap.init_station(stationX, stationY)
PointsOnPathData = coordinationOfPath()
simpleMap.DrawPath(PointsOnPathData)

# simpleMap.initMap(mapX, mapY)
for i in range(0, number_of_drones):
    drone_pos_X = stationX
    drone_pos_Y = stationY
    # drone_pos_X = random.randrange(mapX)
    # drone_pos_Y = random.randrange(mapY)
    areaStatus[drone_pos_X][drone_pos_Y] = "scouted"
    simpleMap.init_drone(drone_pos_X, drone_pos_Y)
    added_drone = drone.Drone(i, drone_width_Of_View, drone_battery, drone_pos_X, drone_pos_Y, 0, 0, 0, 0)
    drones.append(added_drone)


def resetMap(self):
    areaStatus = [["not scouted" for y in range(mapY)] for x in range(mapX)]
    return areaStatus


def randomPath(x, y):
    nextMoveValid = False
    i = 0
    while nextMoveValid == False:
        decision = random.randint(0, 3)
        # go up
        if decision == 0:
            if y < mapY - 1:
                if areaStatus[x][y + 1] != "scouted" or i > 10:
                    return x, y + 1
                else:
                    i += 1
        # go right
        elif decision == 1:
            if x < mapX - 1:
                if areaStatus[x + 1][y] != "scouted" or i > 10:
                    return x + 1, y
                else:
                    i += 1
        # go down
        elif decision == 2:
            if y > 0:
                if areaStatus[x][y - 1] != "scouted" or i > 10:
                    return x, y - 1
                else:
                    i += 1
        # go left
        elif decision == 3:
            if x > 0:
                if areaStatus[x - 1][y] != "scouted" or i > 10:
                    return x - 1, y
                else:
                    i += 1


def SearchingPointsForDrone(PointsOnPathData, VisitedPointsOnPath):
    x_coordiateDiff = 0
    Y_coordiateDiff = 0
    VisitedPointsOnPath.append((0, 0))

    for i in range(0, len(PointsOnPathData)):
        x_coordinate = int(PointsOnPathData[i][0])
        y_coordinate = int(PointsOnPathData[i][1])

        # When i is 0 we are in the beginning of array
        if i == 0:
            x_coordinateOLD = int(PointsOnPathData[i][0])
            y_coordinateOLD = int(PointsOnPathData[i][1])
        else:
            x_coordinateOLD = int(PointsOnPathData[i - 1][0])
            y_coordinateOLD = int(PointsOnPathData[i - 1][1])
            x_coordiateDiff = x_coordinate - x_coordinateOLD
            Y_coordiateDiff = y_coordinate - y_coordinateOLD

        if x_coordiateDiff == 1 and Y_coordiateDiff == 1:
            VisitedPointsOnPath.append(PointsOnPathData[i])

        elif x_coordiateDiff > 1 or Y_coordiateDiff > 1 or Y_coordiateDiff < 0:
            if Y_coordiateDiff > 1 and (y_coordinate > y_coordinateOLD) and (y_coordinate != y_coordinateOLD):
                while Y_coordiateDiff > 1:
                    y_coordinateAdded = int(y_coordinateOLD + 1)
                    y_coordinateOLD = y_coordinateAdded
                    x_coordinateAdded = x_coordinate
                    VisitedPointsOnPath.append((x_coordinateAdded, y_coordinateAdded))
                    Y_coordiateDiff = int(y_coordinate - y_coordinateAdded)

            elif Y_coordiateDiff < 0 and (y_coordinate < y_coordinateOLD) and (y_coordinate != y_coordinateOLD):
                while Y_coordiateDiff < 0:
                    y_coordinateAdded = int(y_coordinateOLD - 1)
                    y_coordinateOLD = y_coordinateAdded
                    x_coordinateAdded = x_coordinate
                    VisitedPointsOnPath.append((x_coordinateAdded, y_coordinateAdded))
                    Y_coordiateDiff = int(y_coordinate - y_coordinateAdded)

            elif x_coordiateDiff > 0 and (x_coordinate > x_coordinateOLD) and (x_coordinate != x_coordinateOLD):
                print("eg er her voldd")
                while x_coordiateDiff > 0:
                    x_coordinateAdded = int(x_coordinateOLD + 1)
                    x_coordinateOLD = x_coordinateAdded
                    y_coordinateAdded = y_coordinate
                    VisitedPointsOnPath.append((x_coordinateAdded, y_coordinateAdded))
                    x_coordiateDiff = int(x_coordinate - x_coordinateAdded)

            VisitedPointsOnPath.append((x_coordinate, y_coordinate))
            y_coordinateOLDTOCompare = y_coordinateAdded
        else:
            print("good day")
    return VisitedPointsOnPath


def droneSearchingPath(SimpleMap, areaStatus, tickCount, survivorFound, VisitedPointsOnPath):
    for i in range(0, len(VisitedPointsOnPath)):
        if survivorFound == False:
            x_coordinate1 = VisitedPointsOnPath[i][0]
            y_coordinate1 = VisitedPointsOnPath[i][1]
            print(int(x_coordinate1), int(y_coordinate1))

            if areaStatus[int(x_coordinate1)][int(y_coordinate1)] == "bingo":
                print("Survivor found in ", tickCount, " ticks!")
                survivorFound = True

            else:
                SimpleMap.mark_searched_area(int(x_coordinate1), int(y_coordinate1))
                areaStatus[int(x_coordinate1)][int(y_coordinate1)] = "scouted"
                SimpleMap.mark_searched_area(int(x_coordinate1 + 1), int(y_coordinate1))
                SimpleMap.mark_searched_area(int(x_coordinate1 - 1), int(y_coordinate1))
                SimpleMap.mark_searched_area(int(x_coordinate1), int(y_coordinate1 - 1))
                SimpleMap.mark_searched_area(int(x_coordinate1), int(y_coordinate1 + 1))

                SimpleMap.update_drone_pos(x_coordinate1, y_coordinate1)
                SimpleMap.mark_searched_area(int(x_coordinate1), int(y_coordinate1))
                tickCount += 1

        time.sleep(0.1)


luckySurvivors = 0
tickAvg = 0

for i in range(numberOfSimulations):

    tickCount = 0
    survivorFound = False

    while survivorFound == False:

        # dronePos = base.nextMove()
        # simpleMap.update_drone_pos(dronePos[0], dronePos[1])
        # simpleMap.mark_searched_area(dronePos[0], dronePos[1])
        for drone in drones:
            drone_pos = drone.get_position()
            drone_id = drone.get_id()
            droneX, droneY = randomPath(drone_pos[0], drone_pos[1])
            drone.set_position(droneX, droneY)
            if areaStatus[droneX][droneY] == "bingo":
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

            simpleMap.update_drone_pos(droneX, droneY)
        tickCount += 1

        if tickCount > 100:
            survivorFound = True
            tickAvg += tickCount

print("Simulation finished!")
print("After running ", numberOfSimulations, " simulations")
print("Using ", number_of_drones, " drones")
print(luckySurvivors, " out of ", numberOfSimulations, " survivors were found")
print("On average, it took ", tickAvg / numberOfSimulations, " ticks to find the survivor")

# time.sleep(5)

# for i in range(20):
# dronePosition = PathScheduler.getPath(dronePosition[0], dronePosition[1])
# Draw a drone on the map somehow

# Hiking path is in the code, but to be implemented
# SearchingPointsForDrone(PointsOnPathData, VisitedPointsOnPath)
# droneSearchingPath(simpleMap, areaStatus, tickCount, survivorFound, VisitedPointsOnPath)
