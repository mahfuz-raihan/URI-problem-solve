n = int(input())
count_in = 0
count_out = 0
for i in range(0, n):
	number = int(input())
	if number >= 10 and number <= 20:
		count_in +=1
	else:
		count_out +=1

print("%d in" % count_in)
print("%d out" % count_out)
