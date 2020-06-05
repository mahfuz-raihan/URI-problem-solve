import math

x = int(input()) 
y = int(input())

if x > y:
	small = y
	big = x
else:
	small = x
	big = y

for i in range(small+1, big):
	if i % 5 == 2 or i % 5 == 3:
		print(i)
