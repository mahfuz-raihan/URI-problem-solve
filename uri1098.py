
a, b1, b2, b3 = 0, 1, 2, 3
print("I={0} J={1}".format(a, b1))
print("I={0} J={1}".format(a, b2))
print("I={0} J={1}".format(a, b3))
while a < 0.8:
	i = a + 0.2
	j1 = b1 + 0.2
	j2 = b2 + 0.2
	j3 = b3 + 0.2
	print("I={0:.1f} J={1:.1f}".format(i, j1))
	print("I={0:.1f} J={1:.1f}".format(i, j2))
	print("I={0:.1f} J={1:.1f}".format(i, j3))
	a = i
	b1 = j1
	b2 = j2
	b3 = j3
	
a, b1, b2, b3 = 1, 2, 3, 4
print("I={0} J={1}".format(a, b1))
print("I={0} J={1}".format(a, b2))
print("I={0} J={1}".format(a, b3))
while a < 1.6:
	i = a + 0.2
	j1 = b1 + 0.2
	j2 = b2 + 0.2
	j3 = b3 + 0.2
	print("I={0:.1f} J={1:.1f}".format(i, j1))
	print("I={0:.1f} J={1:.1f}".format(i, j2))
	print("I={0:.1f} J={1:.1f}".format(i, j3))
	a = i
	b1 = j1
	b2 = j2
	b3 = j3

a, b1, b2, b3 = 2, 3, 4, 5
print("I={0} J={1}".format(a, b1))
print("I={0} J={1}".format(a, b2))
print("I={0} J={1}".format(a, b3))
