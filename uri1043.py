numbers = list(map(float, input().strip().split()))[:3]

a = numbers[0]
b = numbers[1]
c = numbers[2]

if (a+b > c) and (b+c > a) and (c+a > b):
    perimeter_of_triangle = a+b+c
    print("Perimetro = %.1f" % perimeter_of_triangle)
else:
    area = ((a+b)/2)*c
    print("Area = %.1f" %area)
