class Drone:
    # properties
    speed = 0
    previous_direction = None
    stationPos = (None, None)
    pos = (None, None)
    widthOfView = None
    battery = None

    personPos = (None, None)
    isChargingNeeded = False

    def __init__(self, width_Of_View, battery, starting_X, starting_Y, person_X, person_Y, station_X, station_Y, ID, moves=[]):
        if width_Of_View % 2 != 1:
            raise Exception("Can only be initialised with ODD number for width_Of_View")
        self.battery = battery
        self.batteryCapacity = battery
        self.pos = (starting_X, starting_Y)
        self.widthOfView = width_Of_View
        self.person = (person_X, person_Y)
        self.stationPos = (station_X, station_Y)
        self.personPos = (person_X, person_Y)
        self.id = ID
        self.isGoingToLastPlace = False
        self.moves = moves

    def drain_battery(self):
        self.battery = self.battery - 1

    def check_battery_status(self):
        """Checks if the battery is enough to follow the path. Otherwise takes the drone back to the station to charge

        Returns:
            boolean: True when the battery is charged enough, False when it is not
        """
        if self.battery > self.calculate_steps_from_station() + int(self.battery * 0.1 + 1):
            self.drain_battery()
            return True
        else:
            # print(f"steps from station: {self.calculate_steps_from_station()}")
            self.drain_battery()
            return False

    def get_position(self):
        return self.pos

    def set_position_to_coordinate(self, x_pos, y_pos):
        self.pos = (x_pos, y_pos)

    def get_id(self):
        return self.id

    def update_position_by_direction(self, direction):
        """Updates the posiion of the drone by a given direction

        Args:
            direction (string): could be: north, west, south, east

        Returns:
            (int, int): the new position of the drone
        """
        if direction:
            if direction.lower() == "north".lower():
                self.pos = (self.pos[0], self.pos[1] + 1)
                return self.pos
            elif direction.lower() == "south".lower():
                self.pos = (self.pos[0], self.pos[1] - 1)
                return self.pos
            elif direction.lower() == "west".lower():
                self.pos = (self.pos[0] - 1, self.pos[1])
                return self.pos
            elif direction.lower() == "east".lower():
                self.pos = (self.pos[0] + 1, self.pos[1])
                return self.pos
        else:
            return self.pos

    def go_to_station(self):
        """Drives the drone back to the station

        Returns:
            (int, int): the new poistion of the drone
        """
        difference = self.calculate_distance(self.pos, self.stationPos)

        if difference[0] != 0:
            if difference[0] > 0:
                self.update_position_by_direction("east")
            else:
                self.update_position_by_direction("west")
        else:
            if difference[1] > 0:
                self.update_position_by_direction("north")
            else:
                self.update_position_by_direction("south")

        difference = self.calculate_distance(self.pos, self.stationPos)
        if difference[0] == 0 and difference[1] == 0:
            self.isChargingNeeded = False
            self.battery = self.batteryCapacity
            self.isGoingToLastPlace = True

        return self.pos

    def go_to_position(self, desired_pos):
        """Drives the drone to the desired position

        Args:
            previous_pos (int,int): _description_

        Returns:
            _type_: _description_
        """
        difference = self.calculate_distance(self.pos, desired_pos)
        if difference[0] != 0:
            if difference[0] > 0:
                return self.update_position_by_direction("east"), self.isGoingToLastPlace
            else:
                return self.update_position_by_direction("west"), self.isGoingToLastPlace
        else:
            if difference[1] > 0:
                return self.update_position_by_direction("north"), self.isGoingToLastPlace
            else:
                return self.update_position_by_direction("south"), self.isGoingToLastPlace

    def next_step(self):
        oldPos = self.pos
        requiredPos = self.moves[0]
        direction = self.calculateDirection(oldPos, requiredPos)

        # CHECKING THE BATTERY LEVEL
        if not self.check_battery_status():
            # print("WE NEED TO CHARGE")
            self.isChargingNeeded = True
            self.lastRequiredPosition = requiredPos
            # return self.go_to_station(), True

        # GOING TO THE STATION TO CHARGE
        if self.isChargingNeeded:
            # self.drain_battery()
            realNewPos = self.go_to_station()
            if self.search_for_people():
                raise Exception("Person has been found!!!!!!!!!!!!!")
            if realNewPos:
                return realNewPos, True
            else:
                self.update_position_by_direction(direction)

        # GOING TO THE LAST PLACE
        elif self.isGoingToLastPlace:
            # self.drain_battery()
            res = self.go_to_position(self.lastRequiredPosition)
            realNewPos = res[0]
            difference = self.calculate_distance(realNewPos, self.lastRequiredPosition)
            if difference[0] == 0 and difference[1] == 0:
                self.isGoingToLastPlace = False
            if self.search_for_people():
                raise Exception("Person has been found!!!!!!!!!!!!!")
            if realNewPos:
                return realNewPos, True
            else:

                self.update_position_by_direction(direction)

        # FOLLOWING THE PATH
        else:
            realNewPos = self.update_position_by_direction(direction)
            self.moves.pop(0)
            if self.search_for_people():
                raise Exception("Person has been found!!!!!!!!!!!!!")
            return realNewPos, False

    def search_for_people(self):
        current_distance = self.calculate_distance(self.pos, self.personPos)
        # print(f"current distance: {abs(current_distance[0]), abs(current_distance[1])}  ")
        if abs(current_distance[0]) <= int(self.widthOfView / 2) and abs(current_distance[1]) <= int(self.widthOfView / 2):
            # print("PERSON HAS BEEN FOUND")
            return True

    def calculate_distance(self, pos_drone, pos_other):
        return (pos_other[0] - pos_drone[0], pos_other[1] - pos_drone[1])

    def calculate_steps_from_station(self):
        difference = self.calculate_distance(self.pos, self.stationPos)
        steps = abs(difference[0]) + abs(difference[1])
        return steps

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

    def charge_batery(self):
        self.battery = self.batteryCapacity

    def __repr__(self):
        if self.battery == 10:

            return "WE NEED TO CHARGE"
        else:
            return f"position: ({self.pos[0]}, {self.pos[1]})  battery:{self.battery}"


# #    north
# west  east
#    south

#      +
#     +|+
#      |
#      |
#      |
#      |
#      |             +
#      ---------------+
#                    +

# drone = Drone(
#     width_Of_View=5,
#     battery=14,
#     #
#     starting_X=10,
#     starting_Y=10,
#     #
#     Station_X=20,
#     Station_Y=20,
#     #
#     person_X=15,
#     person_Y=15,
# )


# def charge_battery(self):

# def move(self, direction):
#     """The basic function of the drone to move to the new position

#     Args:
#         direction (string): north/ west/ south/ east

#     Returns:
#         realNewPos (int, int): the real new position of the drone
#         isCharging (boolean): returns true when the drone goes to the station to charge, false when it follows the path

#     """
#     print()

#     oldPos = self.pos

#     # GOING TO THE STATION TO CHARGE
#     if self.isChargingNeeded:
#         self.drain_battery()
#         realNewPos = self.go_to_station()
#         self.search_for_people()
#         if realNewPos:
#             return realNewPos, True
#         else:
#             self.update_position_by_direction(direction)

#     # BATTERY HAS DRAINED DRONE CANNOT FOLLOW THE PATH, DECIEDES TO FLY TO THE STATION
#     elif not self.update_battery_status():
#         print("WE NEED TO CHARGE")
#         self.isChargingNeeded = True
#         return self.go_to_station(), True

#     # DRONE GO TO THE REQUIRED DIRECTION
#     else:
#         realNewPos = self.update_position_by_direction(direction)
#         if self.search_for_people():
#             raise Exception("Person has been found!!!!!!!!!!!!!")
#         return realNewPos, False


# drone = Drone(
#     width_Of_View=5,
#     battery=14,
#     #
#     starting_X=10,
#     starting_Y=10,
#     #
#     Station_X=20,
#     Station_Y=20,
#     #
#     person_X=15,
#     person_Y=15,
# )
