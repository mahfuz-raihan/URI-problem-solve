
X = int(input())
Y = int(input())

count = 0
for i in range((Y+1), X):
	if (i % 2 != 0):
		count +=i

print(count)
