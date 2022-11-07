class Drone():
    # properties
    speed = 0
    previous_direction = None
    station_pos = (None, None)
    pos = (None, None)
    width_Of_View = None
    battery = None
    person_pos = (None, None)

    def __init__(
        self,
        id,
        width_Of_View,
        battery,
        starting_X,
        starting_Y,
        person_X,
        person_Y,
        Station_X,
        Station_Y,
    ):
        self.id = id
        if width_Of_View % 2 != 1:
            raise Exception("Can only be initialised with ODD number for width_Of_View")
        self.battery = battery
        self.pos = (starting_X, starting_Y)
        self.width_Of_View = width_Of_View
        self.person = (person_X, person_Y)
        self.station_pos = (Station_X, Station_Y)
        self.person_pos = (person_X, person_Y)

    def update_battery_status(self):
        if self.battery > self.calculate_steps_from_station() + 1:
            self.battery = self.battery - 1
            return True
        else:
            print(f"steps from station: {self.calculate_steps_from_station()}")
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
        print()

        if not self.update_battery_status():
            print("WE NEED TO CHARGE")
            return "we need to charge"
        else:
            self.update_position(direction)
            self.search_for_people()

    def search_for_people(self):
        current_distance = self.calculate_distance(self.pos, self.person_pos)
        print(
            f"current distance: {abs(current_distance[0]), abs(current_distance[1])}  "
        )
        if abs(current_distance[0]) < int(self.width_Of_View / 2) or abs(
            current_distance[1]
        ) < int(self.width_Of_View / 2):
            print("PERSON HAS BEEN FOUND")

    def __repr__(self):
        if self.battery == 10:
            return "WE NEED TO CHARGE"
        else:
            return f"position: ({self.pos[0]}, {self.pos[1]})  battery:{self.battery}"

    def calculate_distance(self, pos_drone, pos_other):
        return (pos_other[0] - pos_drone[0], pos_other[1] - pos_drone[1])

    def calculate_steps_from_station(self):
        difference = self.calculate_distance(self.pos, self.person_pos)
        steps = abs(difference[0]) + abs(difference[1])
        return steps

    def get_position(self):
        return self.pos

    def set_position(self, x_pos, y_pos):
        self.pos = (x_pos, y_pos)

    def get_id(self):
        return self.id

    # def charge_battery(self):


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
"""
drone = Drone(
    width_Of_View=5,
    battery=14,
    #
    starting_X=10,
    starting_Y=10,
    #
    Station_X=20,
    Station_Y=20,
    #
    person_X=15,
    person_Y=15,
)

print("starting postition:")
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
"""