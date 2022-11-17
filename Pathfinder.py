import random

def coordinationOfPath():
    PointsOnPathData = [
        (0.15, 0.31),
        (0.15, 5.60),
        (2.26, 5.60),
        (1.62, 8.81),
        (2.39, 9.91),
        (3.10, 10.25),
        (4, 11.19),
        (4.06, 13.12),
        (3.61, 14.02),
        (5.54, 14.92),
        (7.26, 15.82),
        (8.05, 16.66),
        (9.16, 16.99),
        (9.85, 18.27),
        (11.00, 17.82),
        (13.45, 19.04),
        (13.58, 18.01),
        (12.81, 16.4),
        (13.77, 15.18),
        (14.54, 13.83),
        (14.93, 11.83),
        (18.02, 12.48),
        (19.69, 13.25),
        (21.23, 13.51),
        (22.00, 13.19),
        (23.51, 12.88),
        (24.51, 12.00),
        (26.12, 13.96),
        (27.34, 16.14),
        (28.11, 18.01),
    ]

    return PointsOnPathData

def getRealisticlyLost(mapSizeX,mapSizeY):
    
    floatingPoints = coordinationOfPath()
    
    # Let's assume that it's 0.8 of chance a person will be somewhere close to th hiking path
    mainThreshold = 80
    
    mainProbability = random.randint(0,99)
    
    if(mainProbability > mainThreshold):
        lostX = random.randint(0, mapSizeX - 1)
        lostY = random.randint(0, mapSizeY - 1)
        
    else:
        # Max Distance from hiking path, hardcoded for now
        radius = 20 #squared
        distance = random.randint(0, radius)
        
        # Let's pick a random point from the hiking path
        p = random.randint(0, len(floatingPoints)-1)
        base = floatingPoints[p]
        baseX = int(base[0])
        baseY = int(base[1])
        
        # Let's get some boudaries for base point offfset so we're not out of bounds
        minX = baseX
        maxX = mapSizeX - baseX
        
        minY = baseY
        maxY = mapSizeY - baseY
        
        # Decicde the ratio between vector x and Y
        vectorX = random.randint(0, distance)
        vectorY = distance - vectorX
        
        #Decide directions of vectors
        direction = random.randint(0, 3)
        
        if(direction == 0):
            # X positive, Y positive
            lostX = baseX + min(maxX, vectorX)
            lostY = baseY + min(maxY, vectorY)
            
        elif(direction == 1):
            # X positive, Y negative
            lostX = baseX + min(maxX, vectorX)
            lostY = baseY - min(minY, vectorY)
            
        elif(direction == 2):
            # X negative, Y X positive
            lostX = baseX - min(minX, vectorX)
            lostY = baseY + min(maxY, vectorY)
            
        else:
            # X negative, Y negative
            lostX = baseX - min(minX, vectorX)
            lostY = baseY - min(minY, vectorY)
               
    return [lostX, lostY]
    