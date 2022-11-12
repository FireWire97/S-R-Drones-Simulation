import bullshitmap
import sys
import random
import time
from datetime import datetime

map_x = 4
map_y = 12
mapXX = 60
mapYY = 36

# PathScheduler = Path.Path()
SimpleMap = bullshitmap.BullshitMap()

# areaStatus = [["not scouted"] * mapY] * mapX
areaStatus = [["not scouted" for y in range(mapXX)] for x in range(mapYY)]

DroneX = 22
DroneY = 13
LostX = 15
LostY = 8


areaStatus[DroneX][DroneY] = "scouted"
areaStatus[LostX][LostY] = "bingo"


SimpleMap.initMap(mapXX, mapYY)
SimpleMap.init_drone(DroneX, DroneY, 1)
SimpleMap.init_lost_person(LostX, LostY)
time.sleep(2)

tickCount = 0
survivorFound = False


def snake_algoithm_generator(
    map_x,
    map_y,
    drone_x,
    drone_y,
    shift_left_bottom_corner_by_x,
    shift_left_bottom_corner_by_y,
):
    ############## Variables used for pathQuickScan
    flagTop = 0  # if 0: goes upward, if 1: goes downward
    posFlagFo = 1  # the next two variables: chooses which direction drone starts
    posFlagUp = 1
    posFlagBa = 0  # the next two, set to 0 to start
    posFlagDo = 0
    flag = 1  # set to 0 to start

    steps = int(map_x * (map_y + 1.5))
    steps_array = []
    for step in range(steps):

        if posFlagFo == 1:  # Checks if the drone should move forward (+X)
            drone_x = drone_x + 1  # Moves drone forward on X scale
            if drone_x >= map_x - 1:  # Checks if the drone has reached maximum X
                posFlagFo = 0
                if flagTop == 1:  # Checks it the drone should be going down
                    posFlagDo = 1  # Makes next move of drone go up
                else:
                    posFlagUp = 1  # Makes next move of drone go down

        elif posFlagUp == 1:  # Checks if the drone should move up (+Y)
            drone_y = drone_y + 1  # Moves done up
            flag = flag + 1  # Flag used to make the drone skip lines going up
            if drone_y >= map_y - 1:  # Checks if the drone has reached maximum Y
                posFlagUp = 0
                flagTop = 1  # The drone has reached the top and should go down
                flag = flag - 1  # Has the drone skip correct amount of lines
                if drone_x <= 0:  # Checks if the drone has reached minimum X
                    posFlagFo = 1  # Makes next move of drone go forward
                else:
                    posFlagBa = 1  # Makes next move of drone go backward
            if flag >= 2:  # Checks if the drone has skipped enough lines
                flag = 0  # Reset the flag stated above
                posFlagUp = 0
                if drone_x <= 0:  # Checks if the drone has reached minimum X
                    posFlagFo = 1  # Makes next move of drone go forward
                else:
                    posFlagBa = 1  # Makes next move of drone go backward

        elif posFlagBa == 1:  # Checks if the drone should move back (-X)
            drone_x = drone_x - 1  # Makes drone move backward on X scale
            if drone_x <= 0:  # Checks if drone has reached minimum X
                posFlagBa = 0
                if flagTop == 1:  # Checks if the drone should go up or down next
                    posFlagDo = 1
                else:
                    posFlagUp = 1

        elif posFlagDo == 1:  # Checks if the drone should be going down (-Y)
            drone_y = drone_y - 1  # Moves drone down on Y scale
            flag = flag + 1  # Skip line flag
            if drone_y <= 0:  # Checks to see if drone has reached bottom of map
                posFlagDo = 0
                flagTop = 0  # Drone should next move upwards
                flag = flag - 1  # Makes drone go to unsearched line
                if drone_x <= 0:  # Checks if drone has reached minimum X
                    posFlagFo = 1  # Makes next move go forward
                else:
                    posFlagBa = 1  # Makes next move go backward
            if flag >= 2:  # Checks if the drone has skipped enough lines
                flag = 0  # Reset the flag stated above
                posFlagDo = 0
                if drone_x <= 0:  # Checks if the drone has come back to minimum X
                    posFlagFo = 1  # Makes next move forward
                else:
                    posFlagBa = 1  # Makes next move backward
        steps_array.append((drone_x + shift_left_bottom_corner_by_x, drone_y + shift_left_bottom_corner_by_y))
    return steps_array


# steps = snake_algoithm_generator(map_x, map_y, 0, 0, 10, 10)

# while survivorFound == False:
#     # print( (areaStatus[1]) )
#     # DroneX,DroneY = randomPath(DroneX,DroneY)

#     ############################### Path for 'Quick scan'- can be put in a function

#     #######################################################################

#     drone_x, drone_y = steps.pop(0)
#     SimpleMap.update_drone_pos(drone_x, drone_y, 0)
#     if areaStatus[drone_x][drone_y] == "bingo":
#         print("Survivor found in ", tickCount, " ticks!")
#         survivorFound = True
#     else:
#         SimpleMap.mark_searched_area(drone_x, drone_y)
#         areaStatus[drone_x][drone_y] = "scouted"
#         tickCount += 1
#     SimpleMap.update_map()
#     print(f"drone:   {drone_x}, {drone_y}")
