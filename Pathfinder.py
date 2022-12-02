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

def getIntigerPoints():
    points = [
        (0, 4),
        (0, 6),
        (2, 6),
        (2, 9),
        (2, 10),
        (3, 10),
        (4, 11),
        (4, 13),
        (4, 14),
        (6, 15),
        (7, 16),
        (8, 17),
        (9, 17),
        (10, 18),
        (11, 18),
        (13, 19),
        (14, 18),
        (13, 16),
        (14, 15),
        (15, 14),
        (15, 12),
        (18, 12),
        (20, 13),
        (21, 14),
        (22, 13),
        (24, 13),
        (25, 12),
        (26, 14),
        (27, 16),
        (28, 18),
    ]

    return points

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

def pathfollow_algoithm_generator(mapX, mapY, stationX, stationY, numberOfDrones):
    localAreaStatus = [["not scouted" for y in range(mapY)] for x in range(mapX)]
    tempPointsToSearch = []
    points = getIntigerPoints()
    result = [[]]
    pos = [(stationX, stationY) for u in range(numberOfDrones)]
    localAreaStatus[stationX][stationY] = "scouted"
    # droneOffset = [[]]
    smolArr = []
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
    arr5 = []
    
    offsetLimit = 60
    
    
    if numberOfDrones == 1:
        droneOffset = [(-1,1,-1,1)]
    elif numberOfDrones == 2:
        droneOffset = [(-1,0,-1,0),(0,1,0,1)]
    elif numberOfDrones == 3:
        droneOffset = [(-1,1,-1,1),(-1,0,0,1),(0,1,-1,0)]
    elif numberOfDrones == 4:
        droneOffset = [(-1,0,-1,0),(-1,0,0,1),(0,1,-1,0),(0,1,0,1)]
    elif numberOfDrones == 5:
        droneOffset = [(random.randint(-1,1),random.randint(-1,1),random.randint(-1,1),random.randint(-1,1)) for p in range(numberOfDrones)]
    else:
        return 0
        
    # Offset from the trail
    for offset in range(offsetLimit):
        
        #Going through all the points in the trail
        for i in range(len(points)):
            for drone in range(numberOfDrones):
                #Points to be scouted (don't include transit points)
                tempPointsToSearch = []
                for j in range(min(pos[drone][0], points[i][0] + (offset * droneOffset[drone][0])),
                               max(pos[drone][0], points[i][0] + (offset * droneOffset[drone][1]))):
                    for k in range(min(pos[drone][1], points[i][1] + (offset * droneOffset[drone][2])),
                                   max(pos[drone][1], points[i][1] + (offset * droneOffset[drone][3]))):
                        if j <= 0:
                            j = 0
                        if k <= 0:
                            k = 0
                        if j >= mapX:
                            j = mapX - 1
                        if k >= mapY:
                            k = mapY - 1
                        # if j >= 0 and j < mapX and k >= 0 and k < mapY:
                        if localAreaStatus[j][k] == "not scouted":
                            tempPointsToSearch.append((j,k))
                                
                if len(tempPointsToSearch) == 0:
                    extraPoint = (stationX, stationY)
                    while localAreaStatus[extraPoint[0]][extraPoint[1]] == "scouted" and localAreaStatus.__contains__("not scouted"):
                        # tryhardCounter += 1
                        # for extraX in range(mapX):
                        #     for extraY in range(mapY):
                        extraPoint = (random.randint(0,mapX-1), random.randint(0,mapY-1))

                    # if tryhardCounter >= mapX * mapY:
                    #     tryhardCounter = 9999
                    #
                    # if tryhardCounter < mapX * mapY:
                    tempPointsToSearch.append(extraPoint)
                    
                                
                while(len(tempPointsToSearch) != 0):
                    d = 9999
                    bestd = 9999
                    index = 0
                    #Find closest pint to the pos
                    for l in range(len(tempPointsToSearch)):
                        d = abs(pos[drone][0] - tempPointsToSearch[l][0]) + abs(pos[drone][1] - tempPointsToSearch[l][1])
                        if d < bestd:
                            index = l
                            bestd = d
                
                    while pos[drone] != tempPointsToSearch[index]:
                        if pos[drone][0] != tempPointsToSearch[index][0]:
                            if pos[drone][0] > tempPointsToSearch[index][0]:
                                pos[drone] = (pos[drone][0] - 1, pos[drone][1])
                                localAreaStatus[pos[drone][0]][pos[drone][1]] = "scouted"
                            else:
                                pos[drone] = (pos[drone][0] + 1, pos[drone][1])
                                localAreaStatus[pos[drone][0]][pos[drone][1]] = "scouted"
                        else:
                            if pos[drone][1] > tempPointsToSearch[index][1]:
                                pos[drone] = (pos[drone][0], pos[drone][1] - 1)
                                localAreaStatus[pos[drone][0]][pos[drone][1]] = "scouted"
                            else:
                                pos[drone] = (pos[drone][0], pos[drone][1] + 1)
                                localAreaStatus[pos[drone][0]][pos[drone][1]] = "scouted"
                        
                        # result[drone].append(pos[drone])
                        if drone == 0:
                            arr1.append(pos[drone])
                        if drone == 1:
                            arr2.append(pos[drone])
                        if drone == 2:
                            arr3.append(pos[drone])
                        if drone == 3:
                            arr4.append(pos[drone])
                        if drone == 4:
                            arr5.append(pos[drone])
                    
                    tempPointsToSearch.remove(pos[drone])
        
    # I HATE PYTHON
    # I know it's ugly I'm just fed up with arrays
    # Feel free to make it nicer :)))
    
    if numberOfDrones == 0:
        result =[arr1]
    if numberOfDrones == 1:
        result =[arr1, arr2]
    if numberOfDrones == 2:
        result =[arr1, arr2, arr3]
    if numberOfDrones == 3:
        result =[arr1, arr2, arr3, arr4]
    if numberOfDrones == 4:
        result =[arr1, arr2, arr3, arr4, arr5]
    return result
    
def moveFromAtoB(pointA, pointB):
    path = []
    while pointA != pointB:
        if pointA[0] != pointB[0]:
            if pointA[0] > pointB[0]:
                pointA = (pointA[0] - 1, pointA[1])
                path.append(pointA)
            else:
                pointA = (pointA[0] + 1, pointA[1])
                path.append(pointA)
        else:
            if pointA[1] > pointB[1]:
                pointA = (pointA[0], pointA[1] - 1)
                path.append(pointA)
            else:
                pointA = (pointA[0], pointA[1] + 1)
                path.append(pointA)
      
    return path
                
                
    def SearchingPointsForDrone(PointsOnPathData, VisitedPointsOnPath):
        x_coordiateDiff = 0
    Y_coordiateDiff = 0
    VisitedPointsOnPath.append((0, 0))

    for i in range(0, len(PointsOnPathData)):
        x_coordinate = int(PointsOnPathData[i][0])
        y_coordinate = int(PointsOnPathData[i][1])

        # When i is 0 we are in the beginning of array
        if i == 0:
            x_coordinateOLD = int(PointsOnPathData[i][0])
            y_coordinateOLD = int(PointsOnPathData[i][1])
        else:
            x_coordinateOLD = int(PointsOnPathData[i - 1][0])
            y_coordinateOLD = int(PointsOnPathData[i - 1][1])
            x_coordiateDiff = x_coordinate - x_coordinateOLD
            Y_coordiateDiff = y_coordinate - y_coordinateOLD

        if x_coordiateDiff == 1 and Y_coordiateDiff == 1:
            VisitedPointsOnPath.append(PointsOnPathData[i])

        elif x_coordiateDiff > 1 or Y_coordiateDiff > 1 or Y_coordiateDiff < 0:
            if Y_coordiateDiff > 1 and (y_coordinate > y_coordinateOLD) and (y_coordinate != y_coordinateOLD):
                while Y_coordiateDiff > 1:
                    y_coordinateAdded = int(y_coordinateOLD + 1)
                    y_coordinateOLD = y_coordinateAdded
                    x_coordinateAdded = x_coordinate
                    VisitedPointsOnPath.append((x_coordinateAdded, y_coordinateAdded))
                    Y_coordiateDiff = int(y_coordinate - y_coordinateAdded)

            elif Y_coordiateDiff < 0 and (y_coordinate < y_coordinateOLD) and (y_coordinate != y_coordinateOLD):
                while Y_coordiateDiff < 0:
                    y_coordinateAdded = int(y_coordinateOLD - 1)
                    y_coordinateOLD = y_coordinateAdded
                    x_coordinateAdded = x_coordinate
                    VisitedPointsOnPath.append((x_coordinateAdded, y_coordinateAdded))
                    Y_coordiateDiff = int(y_coordinate - y_coordinateAdded)

            elif x_coordiateDiff > 0 and (x_coordinate > x_coordinateOLD) and (x_coordinate != x_coordinateOLD):
                print("eg er her voldd")
                while x_coordiateDiff > 0:
                    x_coordinateAdded = int(x_coordinateOLD + 1)
                    x_coordinateOLD = x_coordinateAdded
                    y_coordinateAdded = y_coordinate
                    VisitedPointsOnPath.append((x_coordinateAdded, y_coordinateAdded))
                    x_coordiateDiff = int(x_coordinate - x_coordinateAdded)

            VisitedPointsOnPath.append((x_coordinate, y_coordinate))
            y_coordinateOLDTOCompare = y_coordinateAdded
        else:
            print("good day")
    return VisitedPointsOnPath
