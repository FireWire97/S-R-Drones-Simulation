#import map
import SimulationParameters

class Path:
    
    droneRange = 0
    
    mapWidth = 100
    mapLength = 100
    
    
    # Path should keep the information about which area has been scouted
    scoutedArea = [["unknown"] * mapLength] * mapWidth
    
    def __init__(self):
        self.droneRange = SimulationParameters.DetectionRadius
        
    ## Assume map 0,0 point is here
                # ----------------
                # |              |
                # |              |
                # |              |
                # |              |
                # |+             |
                # ----------------
                
                
    def getPath(self, VerticalPos, HorizontalPos):
        if VerticalPos > self.mapLength or HorizontalPos > self.mapWidth:
            return "error"
        else:
            # Try moving up
            if VerticalPos + self.droneRange <= self.mapLength:
                if self.scoutedArea[HorizontalPos, VerticalPos + self.droneRange] == "unknown":
                    return "up"
            # Try moving right
            if HorizontalPos + self.droneRange <= self.map:
                if self.scoutedArea[HorizontalPos, VerticalPos + self.droneRange] == "unknown":
                    return "up"

# Path flow
# - Get current drone location
# - Check if area above, below has been scouted...
# - Go to undiscovered area
# - If not go up until find unscouted area or hit the boundary
# - If hit the boundary, go to the random direction
