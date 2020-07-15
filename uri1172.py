
x = []
for i in range(0, 10):
	number = int(input())
	x.append(number)

for i in range(len(x)):
	if x[i] == 0 or x[i] < 0:
		print("X[{0}] = 1".format(i))
	else:
		print("X[{0}] = {1}".format(i, x[i]))
