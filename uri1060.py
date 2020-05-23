numbers_list = []
count = 0
for i in range(0,6):
	number = float(input())
	numbers_list.append(number)
	if number > 0:
		count +=1
		

print("%d valores positivos" %count)
