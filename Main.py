import Path
#import mapForTrail
import bullshitmap
import random
import time
import drone

mapX = 60
mapY = 36
drone_width_Of_View = 21
drone_battery = 100
number_of_drones = 2
drones = []

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

#dummy drone
#dronePosition = (20,30)

#PathScheduler = Path.Path()
SimpleMap = bullshitmap.BullshitMap()
areaStatus = [["not scouted" for y in range(mapY)] for x in range(mapX)]
LostX = random.randrange(mapX)
LostY = random.randrange(mapY)

SimpleMap.initMap(mapX, mapY)
for i in range(0,number_of_drones):
    drone_pos_X = random.randrange(mapX)
    drone_pos_Y = random.randrange(mapY)
    areaStatus[drone_pos_X][drone_pos_Y] = "scouted"
    SimpleMap.init_drone(drone_pos_X, drone_pos_Y)
    added_drone = drone.Drone(i,drone_width_Of_View,drone_battery,drone_pos_X,drone_pos_Y,0,0,0,0)
    drones.append(added_drone)

areaStatus[LostX][LostY] = "bingo"
SimpleMap.init_lost_person(LostX ,LostY)

tickCount = 0
survivorFound = False

while(survivorFound == False):
    for drone in drones:
        drone_pos = drone.get_position()
        drone_id = drone.get_id()
        DroneX,DroneY = randomPath(drone_pos[0],drone_pos[1])
        areaStatus[DroneX][DroneY] = "scouted"
        drone.set_position(DroneX,DroneY)
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


