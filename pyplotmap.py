import matplotlib.pyplot as plt


class PyplotMap:
    def initMap(self, width_of_map, height_of_map):
        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.img = plt.imread("trail.png")
        self.drawing = self.ax.imshow(self.img, extent=[0, width_of_map, 0, height_of_map])
        # plt.waitforbuttonpress()

    def init_drone(self, drone_x, drone_y, number_of_drones):
        self.drone_plotters = []
        for drone_plotter in range(number_of_drones):
            (drone_plot,) = self.ax.plot(drone_x, drone_y, marker="s", markersize=10)
            self.drone_plotters.append(drone_plot)
        # plt.waitforbuttonpress()

        # self.ax.imshow(self.img, extent=[0, self.img.shape[1], 0, self.img.shape[0]])
        # self.ax.plot(x, x, '--', linewidth=2, color='firebrick')

    def init_lost_person(self, person_x, person_y):
        self.ax.plot(person_x, person_y, marker="*", markersize=15, color="c")
        # plt.waitforbuttonpress()

    def init_station(self, person_x, person_y):
        self.ax.plot(person_x, person_y, marker="P", markersize=20, color="k")
        # plt.waitforbuttonpress()

    def update_drone_pos(self, drone_x, drone_y, which_drone):
        self.drone_plotters[which_drone].set_xdata(drone_x)
        self.drone_plotters[which_drone].set_ydata(drone_y)

        # plt.waitforbuttonpress()
        # self.fig.clear()

    def DrawPath(self, data):
        x = [p[0] for p in data]
        y = [p[1] for p in data]
        # _, ax = plt.subplots()
        #  self.ax.set_xticks(range(60))
        #   self.ax.set_yticks(range(60))
        self.ax.plot(x, y, "o-", color="blue")

    def update_map(self):
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(0.0003)

    def mark_searched_area(self, X, Y):
        self.ax.plot(X, Y, marker="X", color="red")


# 1498
# 2484
