import Path
import mapForTrail

#dummy drone
dronePosition = (20,30)

PathScheduler = Path.Path()


for i in range(20):
    dronePosition = PathScheduler.getPath(dronePosition[0], dronePosition[1])
    #Draw a drone on the map somehow

print("Hello World!")