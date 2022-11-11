from bullshitmap import BullshitMap
import time

droneX = 4
droneY = 4

map=BullshitMap()
map.initMap(60, 36)
map.init_drone(1,1) 
map.init_lost_person(35,6)
time.sleep(2)

PointsOnPathData = [(0, 0.0), (0.15, 0.31), (0.15, 5.60), (2.26, 5.60), (1.62, 8.81), (2.39, 9.91), (3.10, 10.25), (4, 11.19), (4.06, 13.12), (3.61, 14.02),
        (5.54, 14.92),(7.26, 15.82), (8.05, 16.66), (9.16, 16.99), (9.85, 18.27), (10.69, 17.82), (13.45, 19.04), (13.58, 18.01), (12.81, 16.4),
        (13.77, 15.18), (14.54, 13.83), (14.93, 11.83), (18.02, 12.48), (19.69, 13.25), (21.23, 13.51), (22.84, 13.19),
        (24.51, 11.96), (26.12, 13.96), (27.34, 16.14), (28.11, 18.01)]

map.DrawPath(PointsOnPathData)
   
   
for i in range(0, 20, 1):

    drone_x=droneX
    drone_y=droneY+i
    map.mark_searched_area(drone_x+1, drone_y)
    map.mark_searched_area(drone_x-1, drone_y)

    map.update_drone_pos(drone_x, drone_y) 
    map.mark_searched_area(drone_x, drone_y)
    time.sleep(0.1)
    # print(i)