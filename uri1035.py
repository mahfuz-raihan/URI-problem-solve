values = str(input(""))

number = values.split(" ")
A = int(number[0])
B = int(number[1])
C = int(number[2])
D = int(number[3])

if B > C and D > A and (C+D) > (A+B) and C > 0 and D > 0 and A % 2 == 0:
	print("Valores aceitos");
else:
	print("Valores nao aceitos");

