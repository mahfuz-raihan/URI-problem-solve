n = int(input())


for i in range(0, n):
	count = 0
	value = input().split()
	x = int(value[0])
	y = int(value[1])
	if (x < y):
		small = x
		big = y
	else:
		small = y
		big = x
	for num in range(small+1, big):
		if (num % 2 != 0):
			count += num
	print(count)
	
