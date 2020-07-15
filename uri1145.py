<<<<<<< HEAD
n = input().split()

x = int(n[0])
y = int(n[1])

line = []*x

while y <= :
	line.append(i)
	print(line)
	
	
=======
x, y = input().split()
x = int(x)
y = int(y)

count = 0

for i in range(0, y):
    if count == y:
        break
    line = '' #declare a empty string
    for j in range(0, x):
        if count == y:
            break
        count += 1
        line += str(count)+" " #add the count as string with blank space
    print(line[:-1])
>>>>>>> e51633057851a02efda37a2c9d886f5f4f607293
