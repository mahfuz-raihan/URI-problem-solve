values = list(map(int, input().split()))
a = 'A'
n = 0
total = 0
for i in values:
    if a == 'A':
        a = i
    else:
        if i > 0:
            n = i
            break

for i in range(n):
    total += a
    a += 1

print(total)
