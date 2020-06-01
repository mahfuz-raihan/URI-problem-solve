n = int(input())
for i in range(0, n):
	value = list(map(int, input().strip().split()))[:2]
	x = value[0]
	y = value[1]
	
	
	if y == 0:
		print("divisao impossivel")
	else:
		result = x/y
		
		print("{0:.1f}".format(result))


