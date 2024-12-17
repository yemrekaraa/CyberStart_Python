import math
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0]-point1[0]) ** 2 +(point2[1] - point1[1] ** 2))

points=[(0,0), (3,4), (6,8), (1,2), (5,5)]

distances=[]

for i in range(len(points)):
    for j in range(i +1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        print(f"Mesafe {points[i]} ve {points[j]} arasında: {distance:.2f}")


min_distance = min(distance)
print(f"\nEn kısa mesafe: {min_distance:.2f}")