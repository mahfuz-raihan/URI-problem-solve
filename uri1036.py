#URI 1036
"""
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to calculate the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.
"""
import math

a,b,c = input().split()

A = float(a)
B = float(b)
C = float(c)

D = B**2-4*A*C # is the discriments of the quadratic equation


if (A == 0) or (D < 0):
    print("Impossivel calcular")
else:
    r = math.sqrt(D)
    x = (-B+r)/(2*A)
    y = (-B-r)/(2*A)
    
    print("R1 = %.5f" %x)
    print("R2 = %.5f" %y)
