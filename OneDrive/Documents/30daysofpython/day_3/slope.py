#task 8 and 9
m = 2  
b = -2  

slope_task8 = m

y_intercept = (0, m * 0 + b)

x_intercept = (-b / m, 0)

print(f"Slope: {slope_task8}")
print(f"y-intercept: {y_intercept}")
print(f"x-intercept: {x_intercept}")

x1, y1 = 2, 2
x2, y2 = 6, 10

slope_task9 = (y2 - y1) / (x2 - x1)

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"Slope between points (2, 2) and (6, 10): {slope_task9}")
print(f"Distance between points (2, 2) and (6, 10): {distance:.3f}")

print(slope_task8 == slope_task9)