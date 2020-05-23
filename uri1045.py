numbers = list(map(float, input().strip().split()))[:3] # input a list with floating number

numbers.sort(reverse = True) #sort the list with reverse order

a = numbers[0] #list index assign in a variavle
b = numbers[1] #list index assign in b variavle
c = numbers[2] #list index assign in c variavle

if(a >= b+c):
    print("NAO FORMA TRIANGULO")
elif(a**2 == b**2+c**2):
    print("TRIANGULO RETANGULO")
elif(a**2 > b**2+c**2):
    print("TRIANGULO OBTUSANGULO")
elif(a**2 < b**2+c**2):
    print("TRIANGULO ACUTANGULO")

#another condition should be apply here.
if(a == b == c):
     print("TRIANGULO EQUILATERO")
elif(a == b or b == c or c == a):
    print("TRIANGULO ISOSCELES")
