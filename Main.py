#import Path
#import mapForTrail
import bullshitmap
import sys
import random
import time
from datetime import datetime

# Testing with command line argument, to choose which route for the drone to go.
#try:
#   pathNumber = int(sys.argv[1])
#   print(pathNumber)
#except:
#   print("Please use 1, 2 or 3 as an argument")
#   sys.exit(1)
#
#if (pathNumber == 1):
#   print("Drone will follow trail and check points of interest")
#elif (pathNumber == 2):
#   print("Drone will quickly scan the area and go over it a few times")
#elif (pathNumber == 3):
#   print("Drone will scan the area thoroughly")
#else:
#   print("Instructions not clear, drone goes around aimlessly")
#
#
# Testing with user input on which path to use:
#blah = input("Which path do you want to follow: 1, 2 or 3?: ")
#print("Path no. ", blah)

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

DroneX = 55
DroneY = 34
LostX = 15
LostY = 11


areaStatus[DroneX][DroneY] = "scouted"
areaStatus[LostX][LostY] = "bingo"



SimpleMap.initMap(mapX, mapY)
SimpleMap.init_drone(DroneX, DroneY)
SimpleMap.init_lost_person(LostX ,LostY)
time.sleep(2)

tickCount = 0
survivorFound = False

############## Variables used for pathQuickScan
flagTop = 0       # if 0: goes upward, if 1: goes downward
posFlagFo = 1     # the next two variables: chooses which direction drone starts
posFlagUp = 0
posFlagBa = 0     # the next two, set to 0 to start
posFlagDo = 0
flag = 0          # set to 0 to start


while(survivorFound == False):
    # print( (areaStatus[1]) )
    # DroneX,DroneY = randomPath(DroneX,DroneY)
      
############################### Path for 'Quick scan'- can be put in a function
   
   if (posFlagFo == 1):       # Checks if the drone should move forward (+X)
      DroneX = DroneX+1       # Moves drone forward on X scale 
      if (DroneX >= mapX-1):  # Checks if the drone has reached maximum X
         posFlagFo = 0
         if (flagTop == 1):   # Checks it the drone should be going down 
            posFlagDo = 1     # Makes next move of drone go up
         else:
            posFlagUp = 1     # Makes next move of drone go down

   elif (posFlagUp == 1):     # Checks if the drone should move up (+Y)
      DroneY = DroneY+1       # Moves done up
      flag = flag+1           # Flag used to make the drone skip lines going up
      if (DroneY >= mapY-1):  # Checks if the drone has reached maximum Y
         posFlagUp = 0
         flagTop = 1          # The drone has reached the top and should go down
         flag = flag-1        # Has the drone skip correct amount of lines
         if (DroneX <= 0):    # Checks if the drone has reached minimum X 
            posFlagFo = 1     # Makes next move of drone go forward    
         else:
            posFlagBa = 1     # Makes next move of drone go backward
      if (flag >= 2):         # Checks if the drone has skipped enough lines
         flag = 0             # Reset the flag stated above
         posFlagUp = 0
         if (DroneX <= 0):    # Checks if the drone has reached minimum X
            posFlagFo = 1     # Makes next move of drone go forward
         else:
            posFlagBa = 1     # Makes next move of drone go backward

   elif (posFlagBa == 1):     # Checks if the drone should move back (-X)
      DroneX = DroneX-1       # Makes drone move backward on X scale
      if (DroneX <= 0):       # Checks if drone has reached minimum X
         posFlagBa = 0
         if (flagTop == 1):   # Checks if the drone should go up or down next
            posFlagDo = 1
         else:
            posFlagUp = 1

   elif (posFlagDo == 1):     # Checks if the drone should be going down (-Y)
      DroneY = DroneY-1       # Moves drone down on Y scale
      flag = flag+1           # Skip line flag
      if (DroneY <= 0):       # Checks to see if drone has reached bottom of map
         posFlagDo = 0
         flagTop = 0          # Drone should next move upwards
         flag = flag-1        # Makes drone go to unsearched line
         if (DroneX <= 0):    # Checks if drone has reached minimum X
            posFlagFo = 1     # Makes next move go forward
         else:
            posFlagBa = 1     # Makes next move go backward
      if (flag >= 2):         # Checks if the drone has skipped enough lines
         flag = 0             # Reset the flag stated above
         posFlagDo = 0        
         if (DroneX <= 0):    # Checks if the drone has come back to minimum X
            posFlagFo = 1     # Makes next move forward
         else:
            posFlagBa = 1     # Makes next move backward
#######################################################################
          
         
   #DroneX = DroneX+1
   #DroneY = DroneY+1


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
