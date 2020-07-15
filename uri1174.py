a = list()

for i in range(0, 100):
	number = input()
	number = float(number)
	a.append(number)

for i in range(len(a)):
	if a[i] <= 10:
		print("A[{0}] = {1:.1f}".format(i, a[i]))
