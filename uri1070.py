x = int(input())

if x % 2 ==0:
	x +=1

for i in range(x, x+10, 2):
	print(i)

if x+10 % 2 !=0:
	print(x+10)
