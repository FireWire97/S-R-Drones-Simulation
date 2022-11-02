class Drone:
    # properties
    speed = 0
    previous_direction = None
    station_pos = (None, None)
    pos = (None, None)
    depthOfView = None
    battery = None

    def __init__(self, depthOfView, battery, X, Y, Station_X, Station_Y):
        self.battery = battery
        self.pos = (X, Y)
        self.depthOfView = depthOfView

    def update_battery_status(self):
        if self.battery > 10:
            self.battery = self.battery - 1
            return True
        else:
            # print("WE NEED TO CHARGE")
            return False

    def update_position(self, direction):
        if direction.lower() == "north".lower():
            self.pos = (self.pos[0], self.pos[1] + 1)
            return
        elif direction.lower() == "south".lower():
            self.pos = (self.pos[0], self.pos[1] - 1)
            return
        elif direction.lower() == "west".lower():
            self.pos = (self.pos[0] - 1, self.pos[1])
            return
        elif direction.lower() == "east".lower():
            self.pos = (self.pos[0] + 1, self.pos[1])

    def move(self, direction):
        if not self.update_battery_status():
            print("WE NEED TO CHARGE")
        else:
            self.update_position(direction)
            self.search_for_people()

    def search_for_people(self):
        if False:
            print("found")

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

drone = Drone(3, 20, 10, 10, 15, 15)

print(drone)
drone.move("north")
print(drone)
drone.move("north")
print(drone)
drone.move("north")
print(drone)
drone.move("north")
print(drone)

drone.move("north")
print(drone)
drone.move("north")
print(drone)
drone.move("north")
print(drone)

drone.move("north")
print(drone)
drone.move("north")
print(drone)
drone.move("north")
print(drone)

drone.move("north")
print(drone)
drone.move("north")
print(drone)
drone.move("north")
print(drone)
