import math

def min_dist(x1, y1, x2, y2, x3, y3):
    numerator = ((y2 - y1) * x3 - (x2 - x1) * y3 + x2 * y1 - y2 * x1)
    
    denominator = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    
    distance = numerator / denominator
    return distance

x1, y1 = 0, 0   
x2, y2 = 3, 3   
x3, y3 = 1, 0 #1/root(2)  
x3, y3 = 0, 1 #-1/root(2)

distance = min_dist(x1, y1, x2, y2, x3, y3)
print(distance)