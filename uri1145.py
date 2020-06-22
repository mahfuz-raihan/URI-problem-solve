x, y = input().split()
x = int(x)
y = int(y)

count = 0

for i in range(0, y):
    if count == y:
        break
    line = ''
    for j in range(0, x):
        if count == y:
            break
        count += 1
        line += str(count)+" "
    print(line[:-1])
