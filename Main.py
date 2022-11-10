from numpy import arange
import Path
#import mapForTrail
import bullshitmap
import random
import time
import math
import numpy as np
from datetime import datetime
from math import sin, cos, sqrt, atan2


# random.seed(datetime.now())

mapX = 60
mapY = 36



def randomPath(x,y):
    nextMoveValid = False
    while(nextMoveValid == False): 
        decision = random.randrange(4)
        #go up
        if(decision == 0):
            if(y < mapY-1):
                if(areaStatus[x][(y+1)] == "not scouted"):
                    return x,y+1
        #go right
        if(decision == 1):
            if(x < mapX-1):
                tempx= x+1
                tempy=y
                if(areaStatus[tempx][tempy] == "not scouted"):
                    return x+1,y              
        #go down
        if(decision == 2):
            if(y > 0):
                if(areaStatus[x][(y-1)] == "not scouted"):
                    return x,y-1
        #go left
        if(decision == 3):
            if(x > 0):
                tempx= x-1
                tempy=y
                if(areaStatus[(x-1)][y] == "not scouted"):
                    return x-1,y
        try:
            if(areaStatus[x+1][(y)] == "scouted" and areaStatus[x-1][(y)] == "scouted" and areaStatus[x][(y+1)] == "scouted" and areaStatus[x][(y-1)] == "scouted" ):
                if bool(random.getrandbits(1)): # horizontal_or_vertical
                    X=x
                    if bool(random.getrandbits(1)): # plus_or_minus
                        Y=y+1
                    else: 
                        Y=y
                else:
                    Y=y
                    if bool(random.getrandbits(1)): # plus_or_minus
                        X=x+1
                    else: 
                        X=x
                if( X<mapX-1 and X>0 and Y<mapY and Y>0):
                    return X,Y
        except:
            print("out of range")
            try:
                if( areaStatus[x][(y+1)] == "scouted" ):
                    return x, y+1

            except:
                try:
                    if( areaStatus[x][(y-1)] == "scouted" ):
                        return x, y-1
                except:
                    try:
                        if( areaStatus[x-1][(y)] == "scouted" ):
                            return x-1, y
                    except:
                        try:
                            if( areaStatus[x+1][(y)] == "scouted" ):
                                return x+1, y
                        except:
                            print('An exception occurred')



     
      
def coordinationOfPath():
    PointsOnPathData = [(0.15, 0.31), (0.15, 5.60), (2.26, 5.60), (1.62, 8.81), (2.39, 9.91), (3.10, 10.25), (4, 11.19), (4.06, 13.12), (3.61, 14.02),
        (5.54, 14.92),(7.26, 15.82), (8.05, 16.66), (9.16, 16.99), (9.85, 18.27), (11.00, 17.82), (13.45, 19.04), (13.58, 18.01), (12.81, 16.4),
        (13.77, 15.18), (14.54, 13.83), (14.93, 11.83), (18.02, 12.48), (19.69, 13.25), (21.23, 13.51), (22.00, 13.19),
        (23.51, 12.88),(24.51, 12.00), (26.12, 13.96), (27.34, 16.14), (28.11, 18.01)]
            
    return PointsOnPathData

#PathScheduler = Path.Path()
SimpleMap = bullshitmap.BullshitMap()

# areaStatus = [["not scouted"] * mapY] * mapX
areaStatus = [["not scouted" for y in range(mapY)] for x in range(mapX)] 


# print(areaStatus)

# DroneX = random.randrange(mapX-1)
# DroneY = random.randrange(mapY-1)
# LostX = random.randrange(mapX-1)
# LostY = random.randrange(mapY-1)

DroneX = 10
DroneY = 10
LostX = 12
LostY = 11


areaStatus[DroneX][DroneY] = "scouted"
areaStatus[LostX][LostY] = "bingo"



SimpleMap.initMap(mapX, mapY)
SimpleMap.init_drone(DroneX, DroneY)
SimpleMap.init_lost_person(LostX ,LostY)
PointsOnPathData = coordinationOfPath()
SimpleMap.DrawPath(PointsOnPathData)
time.sleep(0.1)


tickCount = 0
survivorFound = False

droneX = 0
droneY = 0

VisitedPointsOnPath = []
x_coordiateDiff=0
Y_coordiateDiff=0

def SearchingPointsForDrone(PointsOnPathData, VisitedPointsOnPath):
    x_coordiateDiff=0
    Y_coordiateDiff=0
    VisitedPointsOnPath.append((0,0))

    for i in range(0, len(PointsOnPathData)):
          x_coordinate = int(PointsOnPathData[i][0])
          y_coordinate = int(PointsOnPathData[i][1])
      
      #When i is 0 we are in the beginning of array
          if(i == 0):
                x_coordinateOLD = int(PointsOnPathData[i][0])
                y_coordinateOLD = int(PointsOnPathData[i][1])
          else:
                x_coordinateOLD = int(PointsOnPathData[i-1][0])
                y_coordinateOLD = int(PointsOnPathData[i-1][1])
                x_coordiateDiff = x_coordinate - x_coordinateOLD
                Y_coordiateDiff = y_coordinate - y_coordinateOLD
            
          if (x_coordiateDiff == 1 and Y_coordiateDiff == 1):
                VisitedPointsOnPath.append(PointsOnPathData[i])
            
          elif(x_coordiateDiff > 1 or Y_coordiateDiff > 1 or Y_coordiateDiff < 0):
                if(Y_coordiateDiff > 1 and (y_coordinate > y_coordinateOLD) and (y_coordinate != y_coordinateOLD)):
                      while(Y_coordiateDiff > 1):
                            y_coordinateAdded = int(y_coordinateOLD+1)
                            y_coordinateOLD = y_coordinateAdded
                            x_coordinateAdded = x_coordinate
                            VisitedPointsOnPath.append(
                         (x_coordinateAdded, y_coordinateAdded))
                            Y_coordiateDiff = int(y_coordinate-y_coordinateAdded)
                     
                elif(Y_coordiateDiff < 0 and (y_coordinate < y_coordinateOLD) and (y_coordinate != y_coordinateOLD)):
                      while(Y_coordiateDiff < 0):
                          y_coordinateAdded = int(y_coordinateOLD-1)
                          y_coordinateOLD = y_coordinateAdded
                          x_coordinateAdded = x_coordinate
                          VisitedPointsOnPath.append(
                          (x_coordinateAdded, y_coordinateAdded))
                          Y_coordiateDiff = int(y_coordinate-y_coordinateAdded)
                      
                elif(x_coordiateDiff > 0 and (x_coordinate > x_coordinateOLD) and (x_coordinate != x_coordinateOLD)):
                    print("eg er her voldd")
                    while(x_coordiateDiff > 0):
                         x_coordinateAdded = int(x_coordinateOLD+1)
                         x_coordinateOLD = x_coordinateAdded
                         y_coordinateAdded = y_coordinate
                         VisitedPointsOnPath.append(
                          (x_coordinateAdded, y_coordinateAdded))
                         x_coordiateDiff = int(x_coordinate-x_coordinateAdded)
              

                VisitedPointsOnPath.append((x_coordinate, y_coordinate))
                y_coordinateOLDTOCompare = y_coordinateAdded
          else:
            print("good day")
    return VisitedPointsOnPath


        
def droneSearchingPath(SimpleMap, areaStatus, tickCount, survivorFound, VisitedPointsOnPath):
    for i in range(0,len(VisitedPointsOnPath)):
        if(survivorFound == False):
              x_coordinate1 = VisitedPointsOnPath[i][0]
              y_coordinate1 = VisitedPointsOnPath[i][1]
              print(int(x_coordinate1), int(y_coordinate1))
          
              if(areaStatus[int(x_coordinate1)][int(y_coordinate1)] == "bingo"):
                print("Survivor found in ", tickCount, " ticks!")
                survivorFound = True
    
              else:       
                SimpleMap.mark_searched_area(int(x_coordinate1), int(y_coordinate1))      
                areaStatus[int(x_coordinate1)][int(y_coordinate1)] = "scouted"
                SimpleMap.mark_searched_area(int(x_coordinate1+1), int(y_coordinate1))
                SimpleMap.mark_searched_area(int(x_coordinate1-1), int(y_coordinate1))
                SimpleMap.mark_searched_area(int(x_coordinate1), int(y_coordinate1-1))
                SimpleMap.mark_searched_area(int(x_coordinate1), int(y_coordinate1+1))


                SimpleMap.update_drone_pos(x_coordinate1, y_coordinate1) 
                SimpleMap.mark_searched_area(int(x_coordinate1), int(y_coordinate1))
                tickCount += 1

        time.sleep(0.1)

SearchingPointsForDrone(PointsOnPathData, VisitedPointsOnPath)
droneSearchingPath(SimpleMap, areaStatus, tickCount, survivorFound, VisitedPointsOnPath)

  
time.sleep(2)

tickCount = 0
survivorFound = False

droneX = 4
droneY = 4



#while(survivorFound == False):
 #    print( (areaStatus[1]) )
  #   DroneX,DroneY = randomPath(DroneX,DroneY)
 #   DroneX = DroneX+1
  #  SimpleMap.update_drone_pos(DroneX,DroneY)
   # if(areaStatus[DroneX][DroneY] == "bingo"):
    #    print("Survivor found in ", tickCount, " ticks!")
     #   survivorFound = True
   # else:
    #    SimpleMap.mark_searched_area(DroneX, DroneY)
     #   areaStatus[DroneX][DroneY] = "scouted"
      #  tickCount += 1
    #print(f"drone:   {DroneX}, {DroneY}")

# time.sleep(5)


