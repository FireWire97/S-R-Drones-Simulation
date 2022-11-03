import matplotlib.pyplot as plt
import numpy as np
import random
import time


class BullshitMap:
    # drone_plt, img,fig,ax=None,None,None,None



    def initMap(self):
        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=(10,6))
        self.img = plt.imread("rsz_1map.png")
        self.drawing = self.ax.imshow(self.img, extent=[0, self.img.shape[1], 0, self.img.shape[0]])


    def init_drone(self, drone_x, drone_y):
        self.drone_plt, =self.ax.plot( drone_x, drone_y, marker="s")
        # plt.waitforbuttonpress()

        # self.ax.imshow(self.img, extent=[0, self.img.shape[1], 0, self.img.shape[0]])
        # self.ax.plot(x, x, '--', linewidth=2, color='firebrick') 
        

    def init_lost_person(self, person_x, person_y):
        self.ax.plot(person_x, person_y, marker=5)


    def update_drone_pos(self,drone_x, drone_y):
        self.drone_plt.set_xdata(drone_x)
        self.drone_plt.set_ydata(drone_y)

        self.fig.canvas.draw()
        self.fig.canvas.flush_events() 
        plt.pause(0.0003)

        # plt.waitforbuttonpress()
        # self.fig.clear()

    def mark_searched_area(self,X,Y):
        self.ax.plot(X, Y, marker='X', color='red')











# 1498
# 2484