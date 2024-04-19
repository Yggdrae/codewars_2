def better_than_average(class_points, your_points):
    total_points = 0
    for points in class_points:
        total_points = total_points + points
    return True if total_points/len(class_points) < your_points else 'False'

print(better_than_average([2, 3], 5))
print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))