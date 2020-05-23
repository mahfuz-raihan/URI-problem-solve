n = int(input())
number = []
for i in range(0, n):
	num = int(input())
	number.append(num)
	
for i in range(0, n):	
	if number[i] == 0:
		print("NULL")
	elif number[i] % 2 == 0: 
		if number[i] > 0:
			print("EVEN POSITIVE")
		else:
			print("EVEN NEGATIVE")
	elif number[i] % 2 == 1:
		if number[i] > 0:
			print("ODD POSITIVE")
		else:
			print("ODD NEGATIVE")
		
