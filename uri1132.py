import math

x = int(input()) 
y = int(input())

if x > y:
	small = y
	big = x
else:
	small = x
	big = y
numbers = 0
for i in range(small, big+1):
	if i % 13 != 0:
		numbers += i

print("{}".format(numbers))
