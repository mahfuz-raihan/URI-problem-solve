numbers = []
count =0
total = 0
for i in range(0,6):
	num = float(input())
	numbers.append(num)
	if num > 0:
		count +=1
		total += num

avarage = total/count

print("%d valores positivos" % count)
print("%.1f" %avarage)
	
