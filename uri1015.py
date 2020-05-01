import math
p = list(map(float, input().strip().split()))
p1= list(map(float, input().strip().split()))


line_distance = ((p1[0]-p[0])**2)+((p1[1]-p[1])**2)

result = math.sqrt(line_distance)
print('%.4f' %result)
