import math
a = list(map(float, input().strip().split()))
pi = 3.14159
#rectangle triangle formula and output
rectangle_triangle_formula = (1/2)*(a[0]*a[2])
print('TRIANGULO: %.3f' %rectangle_triangle_formula)

#area of the radius's circle 

radius_circle = pi*a[2]**2
print('CIRCULO: %.3f' %radius_circle)

#area of trapezium folmula and output
trapezium_formula = (1/2)*(a[0]+a[1])*a[2]
print('TRAPEZIO: %.3f' %trapezium_formula)

#area to square formula and output
square = a[1]**2
print('QUADRADO: %.3f' %square)

#area of rectangle 
area_fo_ractangle = a[0]*a[1]
print('RETANGULO: %.3f' %area_fo_ractangle)
