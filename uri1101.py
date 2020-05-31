while True:

	value = input().split()

	m = int(max(value))
	n = int(min(value))

	if n <= 0 or m <= 0:
		break
		
	count = 0
	sn = ""
	for i in range(n, m+1):
		count +=i
		sn += str(i)+" "
	print("{0}Sum={1}".format(sn, count))

