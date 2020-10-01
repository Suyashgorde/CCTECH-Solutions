import math

class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y

def onSegment(p, q, r): 
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and 
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))): 
        return True
    return False
  
def orientation(p, q, r):  
      
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y)) 
    if (val > 0): 
        return 1
    elif (val < 0): 
        return 2
    else: 
        return 0

def doIntersect(p1,q1,p2,q2): 
      
    o1 = orientation(p1, q1, p2) 
    o2 = orientation(p1, q1, q2) 
    o3 = orientation(p2, q2, p1) 
    o4 = orientation(p2, q2, q1) 
  
    if ((o1 != o2) and (o3 != o4)): 
        return True
    if ((o1 == 0) and onSegment(p1, p2, q1)): 
        return True
  
    if ((o2 == 0) and onSegment(p1, q2, q1)): 
        return True
  
    if ((o3 == 0) and onSegment(p2, p1, q2)): 
        return True
    if ((o4 == 0) and onSegment(p2, q1, q2)): 
        return True
    return False

def distance(x1, y1, x2 , y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

def calForOneBuilding(building_coordinates,sun_coordinates):
    sun_x = sun_coordinates[0]
    sun_y = sun_coordinates[1]
    count1 = 0
    count2 = 0
    total_length = 0
    P1, P2, Q1, Q2, R1, R2, S1, S2 = False, False, False, False, False, False, False, False

    for i in range(4):
        if i == 0: #P
            p1 = Point(sun_x, sun_y) 
            q1 = Point(building_coordinates[0][0], building_coordinates[0][1]) 
            p2 = Point(building_coordinates[1][0], building_coordinates[1][1]) 
            q2 = Point(building_coordinates[2][0], building_coordinates[2][1])
            if doIntersect(p1, q1, p2, q2) == False:
                count1 += 1
                P1 = True
            p1 = Point(sun_x, sun_y) 
            q1 = Point(building_coordinates[0][0], building_coordinates[0][1]) 
            p2 = Point(building_coordinates[2][0], building_coordinates[2][1]) 
            q2 = Point(building_coordinates[3][0], building_coordinates[3][1])
            if doIntersect(p1, q1, p2, q2) == False:
                count2 += 1
                P2 = True

        if i == 1: #Q
            p1 = Point(sun_x, sun_y) 
            q1 = Point(building_coordinates[1][0], building_coordinates[1][1]) 
            p2 = Point(building_coordinates[2][0], building_coordinates[2][1]) 
            q2 = Point(building_coordinates[3][0], building_coordinates[3][1])
            if doIntersect(p1, q1, p2, q2) == False:
                count1 += 1
                Q1 = True
            p1 = Point(sun_x, sun_y) 
            q1 = Point(building_coordinates[1][0], building_coordinates[1][1]) 
            p2 = Point(building_coordinates[3][0], building_coordinates[3][1]) 
            q2 = Point(building_coordinates[0][0], building_coordinates[0][1])
            if doIntersect(p1, q1, p2, q2) == False:
                count2 += 1
                Q2 = True

        if i == 2: #R
            p1 = Point(sun_x, sun_y) 
            q1 = Point(building_coordinates[2][0], building_coordinates[2][1]) 
            p2 = Point(building_coordinates[3][0], building_coordinates[3][1]) 
            q2 = Point(building_coordinates[0][0], building_coordinates[0][1])
            if doIntersect(p1, q1, p2, q2) == False:
                count1 += 1
                R1 = True
            p1 = Point(sun_x, sun_y) 
            q1 = Point(building_coordinates[2][0], building_coordinates[2][1]) 
            p2 = Point(building_coordinates[0][0], building_coordinates[0][1]) 
            q2 = Point(building_coordinates[1][0], building_coordinates[1][1])
            if doIntersect(p1, q1, p2, q2) == False:
                count2 += 1
                R2 = True

        if i == 3: #S
            p1 = Point(sun_x, sun_y) 
            q1 = Point(building_coordinates[3][0], building_coordinates[3][1]) 
            p2 = Point(building_coordinates[0][0], building_coordinates[0][1]) 
            q2 = Point(building_coordinates[1][0], building_coordinates[1][1])
            if doIntersect(p1, q1, p2, q2) == False:
                count1 += 1
                S1 = True
            p1 = Point(sun_x, sun_y) 
            q1 = Point(building_coordinates[3][0], building_coordinates[3][1]) 
            p2 = Point(building_coordinates[1][0], building_coordinates[1][1]) 
            q2 = Point(building_coordinates[2][0], building_coordinates[2][1])
            if doIntersect(p1, q1, p2, q2) == False:
                count2 += 1
                S2 = True

    if count1 >= 2 or count2 >=2 :
        if (P1 == True and P2 == True) and (Q1 == True and Q2 == True):
            total_length += distance(building_coordinates[0][0], building_coordinates[0][1], building_coordinates[1][0], building_coordinates[1][1])
        if (Q1 == True and Q2 == True) and (R1 == True and R2 == True):
            total_length += distance(building_coordinates[1][0], building_coordinates[1][1], building_coordinates[2][0], building_coordinates[2][1])
        if (R1 == True and R2 == True) and (S1 == True and S2 == True):
            total_length += distance(building_coordinates[2][0], building_coordinates[2][1], building_coordinates[3][0], building_coordinates[3][1])
        if (S1 == True and S2 == True) and (P1 == True and P2 == True):
            total_length += distance(building_coordinates[3][0], building_coordinates[3][1], building_coordinates[0][0], building_coordinates[0][1])

    return total_length

def calculateLength(building_coordinates, sun_coordinates):
    n = len(building_coordinates)/4
    sun_x = sun_coordinates[0]
    sun_y = sun_coordinates[1]
    new_building1 = []
    new_building2 = []
    total_length = 0
    if n == 1:
        total_length = calForOneBuilding(building_coordinates, sun_coordinates)
    else:
        if distance(sun_x,sun_y, building_coordinates[0][0], building_coordinates[0][1]) > distance(sun_x, sun_y, building_coordinates[4][0], building_coordinates[4][1]):
            if( distance(building_coordinates[4][0], building_coordinates[4][1], building_coordinates[5][0], building_coordinates[5][1]) < 
                distance(building_coordinates[0][0], building_coordinates[0][1], building_coordinates[1][0], building_coordinates[1][1]) ):

                new_building1.append(building_coordinates[4])
                new_building1.append(building_coordinates[5])
                new_building1.append(building_coordinates[6])
                new_building1.append(building_coordinates[7])
                total_length = calForOneBuilding(new_building1, sun_coordinates) #for P
                
                tan_angle = (building_coordinates[7][1] - sun_y) / (building_coordinates[7][0] - sun_x) #Slope
                height_1 = distance(building_coordinates[6][0], building_coordinates[6][1], building_coordinates[7][0], building_coordinates[7][1])
                dist = distance(building_coordinates[7][0], building_coordinates[7][1], building_coordinates[2][0], building_coordinates[2][1])
                shadow_height = height_1 - dist * tan_angle
                
                total_length += distance(building_coordinates[0][0], building_coordinates[0][1], building_coordinates[2][0], building_coordinates[2][1]) - shadow_height
                
                new_building2.append(building_coordinates[0])
                new_building2.append(building_coordinates[1])
                new_building2.append(building_coordinates[2])
                new_building2.append(building_coordinates[3])
                
                total_length += calForOneBuilding(new_building2, sun_coordinates)#for A
            
            elif( distance(building_coordinates[4][0], building_coordinates[4][1], building_coordinates[5][0], building_coordinates[5][1]) > 
                distance(building_coordinates[0][0], building_coordinates[0][1], building_coordinates[1][0], building_coordinates[1][1]) ):

                new_building2.append(building_coordinates[4])
                new_building2.append(building_coordinates[5])
                new_building2.append(building_coordinates[6])
                new_building2.append(building_coordinates[7])

                total_length = calForOneBuilding(new_building2, sun_coordinates)#for P
            else:

                new_building1.append(building_coordinates[0])
                new_building1.append(building_coordinates[1])
                new_building1.append(building_coordinates[2])
                new_building1.append(building_coordinates[3])
                total_length = calForOneBuilding(new_building1, sun_coordinates) #for A

                new_building2.append(building_coordinates[4])
                new_building2.append(building_coordinates[5])
                new_building2.append(building_coordinates[6])
                new_building2.append(building_coordinates[7])

                total_length += calForOneBuilding(new_building2, sun_coordinates) #for P

        elif distance(sun_x,sun_y, building_coordinates[0][0], building_coordinates[0][1]) < distance(sun_x, sun_y, building_coordinates[4][0], building_coordinates[4][1]):
            if( distance(building_coordinates[4][0], building_coordinates[4][1], building_coordinates[5][0], building_coordinates[5][1]) == 
                distance(building_coordinates[0][0], building_coordinates[0][1], building_coordinates[1][0], building_coordinates[1][1]) ):

                new_building1.append(building_coordinates[0])
                new_building1.append(building_coordinates[1])
                new_building1.append(building_coordinates[2])
                new_building1.append(building_coordinates[3])
                total_length = calForOneBuilding(new_building1, sun_coordinates) #for A

                new_building2.append(building_coordinates[4])
                new_building2.append(building_coordinates[5])
                new_building2.append(building_coordinates[6])
                new_building2.append(building_coordinates[7])
                total_length += calForOneBuilding(new_building2, sun_coordinates) #for P
            
            else:
                new_building2.append(building_coordinates[4])
                new_building2.append(building_coordinates[5])
                new_building2.append(building_coordinates[6])
                new_building2.append(building_coordinates[7])
                total_length += calForOneBuilding(new_building2, sun_coordinates) #for P
                
    return total_length

sun_coordinates = [-3.5,1]
building_coordinates = [[4,0],[4,-5],[7,-5],[7,0],[0.4,-2],[0.4,-5],[2.5,-2],[2.5,-5]]

total_length = calculateLength(building_coordinates, sun_coordinates)
    
print(total_length)
