number = 0
count = 0

while count < 2:
	n = float(input())
	if n >= 0 and n <= 10:
		number += n
		count += 1
	else:
		print("nota invalida")
	
result = number / 2
print("media = {0:.2f}".format(result))
