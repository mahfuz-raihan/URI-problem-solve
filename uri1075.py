n = int(input())
count = 2
print(count)
while count < 10000:
	count += n
	if count >= 10000:
		break
	print(count)
