#import map
from math import cos, asin, sqrt, pi
import SimulationParameters
import pandas as pd
import numpy as np
import random

class Path:
    
    droneRange = 0
    
    mapWidthScale = 0
    mapLengthScale = 0
    
    # Not rounded versions for calculations
    mapWidthScaleNR = 0
    mapLengthScaleNR = 0
    
    scoutedArea = [[]]
    
    def __init__(self):
        filename = 'model_windspeed.csv'
        w_dir, w_speed = self.get_weather_data(filename)
        self.droneRange = SimulationParameters.DetectionRadius
        self.initMap()
        self.mapWidthCoordStep = abs(SimulationParameters.Eborderline - SimulationParameters.Wborderline) / self.mapWidthScaleNR
        self.mapLengthCoordStep = abs(SimulationParameters.Nborderline - SimulationParameters.Sborderline) / self.mapLengthScaleNR
        # Line below works only For positive long and negative lat, if we move from Iceland we have to change that
        self.scoutedArea = [[Sector(SimulationParameters.Sborderline + j * self.mapLengthCoordStep, SimulationParameters.Wborderline - i * self.mapWidthCoordStep, random.choice(w_speed), random.choice(w_dir)) for j in range(self.mapLengthScale)] for i in range(self.mapWidthScale)]

    def get_weather_data(self, filename):
        weather_cvs = pd.read_csv(filename, encoding='latin-1')
        raw_data = weather_cvs.values
        cols1 = range(2, 4)
        X1 = raw_data[:, cols1]
        cols2 = range(4, 6)
        X2 = raw_data[:, cols2]
        cols3 = range(6, 8)
        X3 = raw_data[:, cols3]
        wind_direction = np.concatenate((X1[:,0],X2[:,0],X3[:,0]))
        wind_speed = np.concatenate((X1[:,1],X2[:,1],X3[:,1]))
        return wind_direction, wind_speed


    # In this function map is divided into search areas which size is defined by dron detection radius
    def initMap(self):
         # Calculate horizontal distance of the search area
        self.mapWidthScale = self.distance(SimulationParameters.Eborderline, SimulationParameters.Sborderline, SimulationParameters.Wborderline, SimulationParameters.Sborderline)
         # Calculate vertical distance of the search area
        self.mapLengthScale = self.distance(SimulationParameters.Eborderline, SimulationParameters.Nborderline, SimulationParameters.Eborderline, SimulationParameters.Sborderline)
        
        # Convert from km to m
        self.mapWidthScale *= 1000
        self.mapLengthScale *= 1000
        
        # Divide by search radius
        self.mapWidthScaleNR = self.mapWidthScale / SimulationParameters.DetectionRadius
        self.mapLengthScaleNR = self.mapLengthScale / SimulationParameters.DetectionRadius
        self.mapWidthScale = int(self.mapWidthScaleNR)
        self.mapLengthScale = int(self.mapLengthScaleNR)

    # Function used to calculate distances between two points with coordinates
    def distance(self, lat1, lon1, lat2, lon2):
        p = pi/180
        a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
        return 12742 * asin(sqrt(a)) #2*R*asin...
        
                
    # def getCoordinates(self, width, length):
    #     lat = SimulationParameters.Sborderline + length * self.mapLengthScale
    #     lon = SimulationParameters.Nborderline + length * self.mapWidthScale
    #     return [lon, lat]
    
    # def getScaleValues(self, lon, lat):
    #     width = int(SimulationParameters.Sborderline)
                
    def getPath(self, VerticalPos, HorizontalPos):
        
        # Try moving up
        if self.scoutedArea[HorizontalPos][VerticalPos + 1].status == "not scouted":
            return (HorizontalPos, VerticalPos + 1)
        # Try moving right
        if self.scoutedArea[HorizontalPos + 1][VerticalPos].status == "not scouted":
            return (HorizontalPos + 1, VerticalPos)
        # Try moving down
        if VerticalPos > 0:
            if self.scoutedArea[HorizontalPos][VerticalPos - 1].status == "not scouted":
                return (HorizontalPos, VerticalPos - 1)
        # Try moving left
        if HorizontalPos > 0:
            if self.scoutedArea[HorizontalPos - 1][VerticalPos].status == "not scouted":
                return (HorizontalPos - 1, VerticalPos)


class Sector:
    
    longitude = 0
    latitiude = 0
    status = "not initialized"
    wind_speed = 0
    wind_direction = 'C'
    
    
    def __init__(self, long, lat, speed, dir):
        self.longitude = long
        self.latitiude = lat
        self.status = "not scouted"
        self.wind_speed = speed
        self.wind_direction = dir

        
# Path flow
# - Get current drone location
# - Check if area above, below has been scouted...
# - Go to undiscovered area
# - If not go up until find unscouted area or hit the boundary
# - If hit the boundary, go to the random direction
