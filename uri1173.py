n = list()
number = int(input())
for i in range(0, 10):
	n.append(number)
	number *= 2

for i in range(len(n)):
	print("N[{}] = {}".format(i, n[i]))
