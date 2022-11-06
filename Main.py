import Path
#import mapForTrail
import bullshitmap
import random
import time
from datetime import datetime

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



#dummy drone
#dronePosition = (20,30)

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
LostX = 15
LostY = 10


areaStatus[DroneX][DroneY] = "scouted"
areaStatus[LostX][LostY] = "bingo"



SimpleMap.initMap(mapX, mapY)
SimpleMap.init_drone(DroneX, DroneY)
SimpleMap.init_lost_person(LostX ,LostY)
time.sleep(2)

tickCount = 0
survivorFound = False

while(survivorFound == False):
    # print( (areaStatus[1]) )
    # DroneX,DroneY = randomPath(DroneX,DroneY)
    DroneX = DroneX+1
    SimpleMap.update_drone_pos(DroneX,DroneY)
    if(areaStatus[DroneX][DroneY] == "bingo"):
        print("Survivor found in ", tickCount, " ticks!")
        survivorFound = True
    else:
        SimpleMap.mark_searched_area(DroneX, DroneY)
        areaStatus[DroneX][DroneY] = "scouted"
        tickCount += 1
    print(f"drone:   {DroneX}, {DroneY}")

# time.sleep(5)

# for i in range(20):
#     #dronePosition = PathScheduler.getPath(dronePosition[0], dronePosition[1])
#     #Draw a drone on the map somehow
    # SimpleMap.update_drone_pos(DroneX, DroneY)
    # print(DroneX,DroneY)
