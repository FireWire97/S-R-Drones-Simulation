from distutils.file_util import move_file

# from bullshitmap import BullshitMap
from pyplotmap import PyplotMap
import random
from drone import Drone
from snake import snake_algoithm_generator
from Pathfinder import pathfollow_algoithm_generator


class BaseStation:
    def __init__(self, size_of_the_map_x, size_of_the_map_y, number_of_drones, station_pos_x, station_pos_y, lost_person_x, lost_person_y, search_algorithm="pathfollow", drone_battery_capacity=500):
        self.mapX = size_of_the_map_x
        self.mapY = size_of_the_map_y
        self.stationX = station_pos_x
        self.stationY = station_pos_y
        self.numberOfDrones = number_of_drones
        self.searchingAlgorithm = search_algorithm
        self.areaStatus = [["not scouted" for y in range(self.mapY)] for x in range(self.mapX)]
        self.areaStatus[self.stationX][self.stationY] = "scouted"
        self.coveredArea = {}
        self.is_charging_needed_base = False
        self.going_to_last_place = False
        self.listOfMoves = []

        if search_algorithm == "snake":
            for i in range(number_of_drones):
                width = int((1) * (size_of_the_map_x / number_of_drones))
                if i == (number_of_drones - 1):
                    specificWidth = size_of_the_map_x - (i * width)
                    moves = snake_algoithm_generator(
                        specificWidth,
                        size_of_the_map_y,
                        station_pos_x,
                        station_pos_y,
                        (i * width),
                        0,
                    )
                else:
                    moves = snake_algoithm_generator(
                        width,
                        size_of_the_map_y,
                        station_pos_x,
                        station_pos_y,
                        (i * width),
                        0,
                    )
                self.listOfMoves.append(moves)
                
        if search_algorithm == "pathfollow":
            moves = pathfollow_algoithm_generator(
                size_of_the_map_x,
                size_of_the_map_y,
                station_pos_x,
                station_pos_y,
                number_of_drones
            )
            self.listOfMoves.append(moves)

        """++++++++++++++++++++++++++++++++++++++++++
         PUT THE NEW ALGORITHM HERE AND APPEND THE PATH TO THE listOfMoves FOR EVERY DRONE OR GUARANTEE TO RUN THE CODE ONLY WITH VALID PARAMETERS
        ++++++++++++++++++++++++++++++++++++++++++"""

        self.drones = []
        for id in range(0, self.numberOfDrones):
            drone_pos_X = station_pos_x
            drone_pos_Y = station_pos_y
            self.areaStatus[drone_pos_X][drone_pos_Y] = "scouted"
            # SimpleMap.init_drone(drone_pos_X, drone_pos_Y)
            added_drone = Drone(1, drone_battery_capacity, drone_pos_X, drone_pos_Y, lost_person_x, lost_person_y, station_pos_x, station_pos_y, id, moves=self.listOfMoves[id])
            self.drones.append(added_drone)

    def getPositionOfDrones(self):
        """Get the positions of the drones

        Returns:
            [ (int,int) ]: array of the positions of the drones
        """
        dronePositions = []
        for drone in self.drones:
            dronePositions.append(drone.get_position())

        return dronePositions

    def moveOneTime(self):
        """Move the drones to the next position

        Raises:
            Exception: The Person has been fund

        Returns:
            [ (int,int) ]: positions of the drones for plotting
        """
        newPositions = []
        for drone in self.drones:
            try:
                pos, temp = drone.next_step()
                newPositions.append(pos)
            except:
                raise Exception("Person has been found!!!!!!!!!!!!!")

        return newPositions

    # def nextMove(self):
    #     newPositions = []
    #     for drone in self.drones:
    #         oldPos = drone.get_position()

    #         # GOING TO THE LAST PLACE BEFORE CHARGING
    #         if self.going_to_last_place:
    #             realNewPos, self.going_to_last_place = drone.go_to_previous_pos(self.lastPlace)
    #             if self.going_to_last_place == False:
    #                 realNewPos = self.goingToNewPosOfThePath(drone, oldPos)

    #         # GOING TO THE STATION FOR CHARGING
    #         elif self.is_charging_needed_base:
    #             if drone.get_position() != (self.stationX, self.stationY):
    #                 realNewPos, self.is_charging_needed_base = drone.move("north")
    #             else:
    #                 self.is_charging_needed_base = False
    #                 realNewPos, self.going_to_last_place = drone.go_to_previous_pos(self.lastPlace)

    #         # GOING TO THE NEXT NORMAL STEP OF THE PATH
    #         else:
    #             realNewPos = self.goingToNewPosOfThePath(drone, oldPos)

    #         newPositions.append(realNewPos)
    #     return newPositions

    # def goingToNewPosOfThePath(self, drone, oldPos):
    #     newPos = self.moves.pop(0)
    #     # newPos = self.randomPath(oldPos[0], oldPos[1])
    #     realNewPos, self.is_charging_needed_base = drone.move(self.calculateDirection(oldPos, newPos))
    #     self.areaStatus[realNewPos[0]][realNewPos[1]] = "scouted"
    #     # self  .coveredArea.add(self.drone.get_position())
    #     if self.is_charging_needed_base:
    #         self.lastPlace = newPos
    #     return realNewPos

    # if newPos in self.coveredArea:
    #     return newPos
    # else:
    #     self.coveredArea.add(self.drone.get_position())
    #     return newPos,

    # def randomPath(self, x, y):
    #     nextMoveValid = False
    #     while nextMoveValid == False:
    #         decision = random.randrange(4)
    #         # go up
    #         if decision == 0:
    #             if y < self.mapY - 1:
    #                 if self.areaStatus[x][(y + 1)] == "not scouted":
    #                     return x, y + 1
    #         # go right
    #         if decision == 1:
    #             if x < self.mapX - 1:
    #                 tempx = x + 1
    #                 tempy = y
    #                 if self.areaStatus[tempx][tempy] == "not scouted":
    #                     return x + 1, y
    #         # go down
    #         if decision == 2:
    #             if y > 0:
    #                 if self.areaStatus[x][(y - 1)] == "not scouted":
    #                     return x, y - 1
    #         # go left
    #         if decision == 3:
    #             if x > 0:
    #                 tempx = x - 1
    #                 tempy = y
    #                 if self.areaStatus[(x - 1)][y] == "not scouted":
    #                     return x - 1, y
    #         # Get out from a place
    #         try:
    #             if self.areaStatus[x + 1][(y)] == "scouted" and self.areaStatus[x - 1][(y)] == "scouted" and self.areaStatus[x][(y + 1)] == "scouted" and self.areaStatus[x][(y - 1)] == "scouted":
    #                 if bool(random.getrandbits(1)):  # horizontal_or_vertical
    #                     X = x
    #                     if bool(random.getrandbits(1)):  # plus_or_minus
    #                         Y = y + 1
    #                     else:
    #                         Y = y
    #                 else:
    #                     Y = y
    #                     if bool(random.getrandbits(1)):  # plus_or_minus
    #                         X = x + 1
    #                     else:
    #                         X = x
    #                 if X < self.mapX - 1 and X > 0 and Y < self.mapY and Y > 0:
    #                     return X, Y
    #         except:
    #             print("out of range")
    #             try:
    #                 if self.areaStatus[x][(y + 1)] == "scouted":
    #                     return x, y + 1

    #             except:
    #                 try:
    #                     if self.areaStatus[x][(y - 1)] == "scouted":
    #                         return x, y - 1
    #                 except:
    #                     try:
    #                         if self.areaStatus[x - 1][(y)] == "scouted":
    #                             return x - 1, y
    #                     except:
    #                         try:
    #                             if self.areaStatus[x + 1][(y)] == "scouted":
    #                                 return x + 1, y
    #                         except:
    #                             print("An exception occurred")

    # def generate_path(self, droneX, droneY):
    # def calculateDirection(self, oldPos, newPos):
    #     xDiff = newPos[0] - oldPos[0]
    #     yDiff = newPos[1] - oldPos[1]

    #     if xDiff == 1:
    #         return "east"
    #     elif xDiff == -1:
    #         return "west"
    #     elif yDiff == 1:
    #         return "north"
    #     elif yDiff == -1:
    #         return "south"
