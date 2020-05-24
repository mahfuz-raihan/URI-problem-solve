number_list = []
highest = 0
position = 0

for i in range(0, 100):
	value = int(input())
	number_list.append(value)

for i in range(0, 100):
	if number_list[i] > highest:
		highest = number_list[i]
		position = i+1
	else:
		highest = highest
		position = position

print("%d" %highest)
print("%d" %position)
