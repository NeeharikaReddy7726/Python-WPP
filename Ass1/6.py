import random
import math

import random
import math

#euclidean dist
def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

points = [(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]

nearest_neighbors = []

for i, point in enumerate(points):
    min_distance = float('inf')
    nearest_point = None

    for j, other_point in enumerate(points):
        if i != j: 
            distance = euclidean_distance(point, other_point)
            if distance < min_distance:
                min_distance = distance
                nearest_point = other_point

    nearest_neighbors.append((point, nearest_point))

print("Point -> Nearest Neighbor")
for pair in nearest_neighbors:
    print(f"{pair[0]} -> {pair[1]}")
points = [(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]

nearest_neighbors = []

for i, point in enumerate(points):
    min_distance = float('inf')
    nearest_point = None

    for j, other_point in enumerate(points):
        if i != j: 
            distance = euclidean_distance(point, other_point)
            if distance < min_distance:
                min_distance = distance
                nearest_point = other_point

    nearest_neighbors.append((point, nearest_point))

# results
print("Point -> Nearest Neighbor")
for pair in nearest_neighbors:
    print(f"{pair[0]} -> {pair[1]}")