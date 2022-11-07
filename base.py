from bullshitmap import BullshitMap
import random
from drone import Drone

class BaseStation:
    def __init__(self, size_of_the_map_x, size_of_the_map_y, number_of_drones, width_of_view, station_pos_x, station_pos_y, lost_person_x, lost_person_y, search_algorithm="random", drone_battery_capacity=50):
        self.mapX = size_of_the_map_x
        self.mapY = size_of_the_map_y
        self.stationX = station_pos_x
        self.stationY = station_pos_y
        self.numberOfDrones = number_of_drones
        self.searchingAlgorithm = search_algorithm
        self.areaStatus = [["not scouted" for y in range(self.mapY)] for x in range(self.mapX)] 
        self.areaStatus[self.stationX][self.stationY] = "scouted"
        self.coveredArea = {}

        # for index in number_of_drones:
            # print(f'index: {index}')
            # globals()[f"drone_{index}"] =  Drone(1, 10000, self.stationX, self.stationY, lost_person_x, lost_person_y, self.stationX, self.stationY)
    
        self.drone = Drone(1, width_of_view, drone_battery_capacity, self.stationX, self.stationY, lost_person_x, lost_person_y, self.stationX, self.stationY)
        # self.coveredArea.add(self.drone.get_position())

    def randomPath(self, x,y):
            nextMoveValid = False
            while(nextMoveValid == False): 
                decision = random.randrange(4)
                #go up
                if(decision == 0):
                    if(y < self.mapY-1):
                        if(self.areaStatus[x][(y+1)] == "not scouted"):
                            return x,y+1
                #go right
                if(decision == 1):
                    if(x < self.mapX-1):
                        tempx= x+1
                        tempy=y
                        if(self.areaStatus[tempx][tempy] == "not scouted"):
                            return x+1,y              
                #go down
                if(decision == 2):
                    if(y > 0):
                        if(self.areaStatus[x][(y-1)] == "not scouted"):
                            return x,y-1
                #go left
                if(decision == 3):
                    if(x > 0):
                        tempx= x-1
                        tempy=y
                        if(self.areaStatus[(x-1)][y] == "not scouted"):
                            return x-1,y
                # Get out from a place
                try:
                    if(self.areaStatus[x+1][(y)] == "scouted" and self.areaStatus[x-1][(y)] == "scouted" and self.areaStatus[x][(y+1)] == "scouted" and self.areaStatus[x][(y-1)] == "scouted" ):
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
                        if( X<self.mapX-1 and X>0 and Y<self.mapY and Y>0):
                            return X,Y
                except:
                    print("out of range")
                    try:
                        if( self.areaStatus[x][(y+1)] == "scouted" ):
                            return x, y+1

                    except:
                        try:
                            if( self.areaStatus[x][(y-1)] == "scouted" ):
                                return x, y-1
                        except:
                            try:
                                if( self.areaStatus[x-1][(y)] == "scouted" ):
                                    return x-1, y
                            except:
                                try:
                                    if( self.areaStatus[x+1][(y)] == "scouted" ):
                                        return x+1, y
                                except:
                                    print('An exception occurred')


    # def generate_path(self, droneX, droneY):
    def calculateDirection(self, oldPos, newPos):
        xDiff = newPos[0] - oldPos[0]
        yDiff = newPos[1] - oldPos[1]

        if xDiff == 1:
            return "east"
        elif xDiff == -1:
            return "west"
        elif yDiff == 1:
            return "north"
        elif yDiff == -1:
            return "south"

    def getPositionOfDrones(self):
        return self.drone.get_position()

    def nextMove(self):
        oldPos = self.drone.get_position()
        newPos = self.randomPath(oldPos[0], oldPos[1])
        self.areaStatus[ newPos[0] ][ newPos[1] ] = "scouted"
        self.drone.move( self.calculateDirection(oldPos, newPos))
        # self.coveredArea.add(self.drone.get_position())
        return newPos


        # if newPos in self.coveredArea:
        #     return newPos
        # else:
        #     self.coveredArea.add(self.drone.get_position())
        #     return newPos, 