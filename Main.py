import Path
#import mapForTrail
import bullshitmap
import random
import time

mapX = 60
mapY = 36

def randomPath(x,y):
    nextMoveValid = False
    while(nextMoveValid == False): 
        decision = random.randrange(3)
        #go up
        if(decision == 0):
            if(y < mapY):
                if(areaStatus[x][y+1] == "not scouted"):
                    return x,y+1
        #go right
        if(decision == 1):
            if(x < mapX):
                if(areaStatus[x+1][y] == "not scouted"):
                    return x+1,y              
        #go down
        if(decision == 2):
            if(y > 0):
                if(areaStatus[x][y-1] == "not scouted"):
                    return x,y-1
        #go left
        if(decision == 3):
            if(x > 0):
                if(areaStatus[x-1][y] == "not scouted"):
                    return x-1,y

#dummy drone
#dronePosition = (20,30)

#PathScheduler = Path.Path()
SimpleMap = bullshitmap.BullshitMap()

areaStatus = [["not scouted"] * mapY] * mapX
DroneX = random.randrange(mapX)
DroneY = random.randrange(mapY)
LostX = random.randrange(mapX)
LostY = random.randrange(mapY)

areaStatus[DroneX][DroneY] = "scouted"
areaStatus[LostX][LostY] = "bingo"

SimpleMap.initMap(mapX, mapY)
SimpleMap.init_drone(DroneX, DroneY)
SimpleMap.init_lost_person(LostX ,LostY)

tickCount = 0
survivorFound = False

while(survivorFound == False):
    DroneX,DroneY = randomPath(DroneX,DroneY)
    SimpleMap.update_drone_pos(DroneX,DroneY)
    if(areaStatus[DroneX][DroneY] == "bingo"):
        print("Survivor found in ", tickCount, " ticks!")
        survivorFound = True
    else:
        SimpleMap.mark_searched_area(DroneX, DroneY)
        tickCount += 1

# time.sleep(5)

#for i in range(20):
    #dronePosition = PathScheduler.getPath(dronePosition[0], dronePosition[1])
    #Draw a drone on the map somehow
