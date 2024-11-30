def right_angle_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
           print('*', end=' ')
        print()

right_angle_triangle(5)