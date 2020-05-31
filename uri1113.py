while True:
	value = list(map(int, input().strip().split()))
	
	x = value[0]
	y = value[1]
	
	if x == y:
		break
	elif x < y:
		print("Crescente")
	else:
		print("Decrescente")
