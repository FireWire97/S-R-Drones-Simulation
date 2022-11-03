import matplotlib.pyplot as plt
import numpy as np
import random
import time


class BullshitMap:
    drone_plt, img,fig,ax=None,None,None,None
    


    def initMap(self):
        plt.ion()
        # import matplotlib.pyplot as plt
        self.img = plt.imread("map3.png")
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(self.img, extent=[0, self.img.shape[1], 0, self.img.shape[0]])
        time.sleep(5)

    def init_drone(self, drone_x, drone_y):
        # plt.ion()
        # # import matplotlib.pyplot as plt
        # img = plt.imread("map3.png")
        # fig, ax = plt.subplots()
        # # ax.imshow(img)

        # drone  = 1000,1000
        # print ( drone)
        # # # fig, ax = plt.subplots()
        # x = range(500)
        # self.ax.imshow(self.img, extent=[0, self.img.shape[1], 0, self.img.shape[0]])
        # self.ax.plot(x, x, '--', linewidth=2, color='firebrick') 
        
        plt.ion()
        self.drone_plt, =self.ax.plot( drone_x, drone_y, marker=11)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events() 
        plt.waitforbuttonpress()

    def init_lost_person(self, person_x, person_y):
        self.ax.plot(person_x, person_y, marker=5)


    def update_drone_pos(self,drone_x, drone_y):
        plt.ion()
        self.drone_plt.set_ydata(drone_y)
        self.drone_plt.set_xdata(drone_x)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events() 
        # plt.waitforbuttonpress()
        time.sleep(0.5)


droneX = 200
droneY = 200

map=BullshitMap()
map.initMap()
map.init_drone(333,444) 
map.init_lost_person(1200,1200)
time.sleep(2)

for i in range(0,350, 20):

    map.update_drone_pos(droneX+i, droneY+i) 






# plt.ion()
# # import matplotlib.pyplot as plt
# img = plt.imread("map3.png")
# fig, ax = plt.subplots()
# # ax.imshow(img)

# drone  = 1000,1000
# print ( drone)
# # # fig, ax = plt.subplots()
# x = range(500)
# ax.imshow(img, extent=[0, img.shape[1], 0, img.shape[0]])
# ax.plot(x, x, '--', linewidth=2, color='firebrick') 

# drone_plt, =ax.plot( drone[0], drone[1], marker=11)
# fig.canvas.draw()
# fig.canvas.flush_events() 




# for event in range(10):
#     drone = random.randint(0, 1500), random.randint(0, 1500)
#     print(drone)
#     drone_plt.set_ydata(drone[1])
#     drone_plt.set_xdata(drone[0])
#     # ax.plot( drone[0], drone[1], marker=11) 
#     fig.canvas.draw()
#     fig.canvas.flush_events() 
#     # time.sleep(0.5)

#     plt.waitforbuttonpress()










# img = plt.imread("img.png")
# ig, ax = plt.subplots()
# ax.imshow(img)
# plt.ion()
# for i in range(50):
#     y = np.random.random([10,1])
#     plt.plot(y)
#     plt.draw()
#     plt.pause(0.0001)
#     plt.clf()


# 1498
# 2484