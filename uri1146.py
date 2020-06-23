
while True:
    n = int(input())
    if n == 0:
        break
    line = ''
    count = 0
    for i in range(0, n):
        count += 1
        line += str(count)+" "
    print(line[:-1])
