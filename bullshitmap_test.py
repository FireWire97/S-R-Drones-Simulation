from bullshitmap import BullshitMap
import time

droneX = 4
droneY = 4

map=BullshitMap()
map.initMap(60, 36)
map.init_drone(1,1) 
map.init_lost_person(35,6)
time.sleep(2)

for i in range(0, 20, 1):

    drone_x=droneX
    drone_y=droneY+i
    map.mark_searched_area(drone_x+1, drone_y)
    map.mark_searched_area(drone_x-1, drone_y)

    map.update_drone_pos(drone_x, drone_y) 
    map.mark_searched_area(drone_x, drone_y)
    time.sleep(0.1)
    # print(i)