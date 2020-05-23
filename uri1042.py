numbers = list(map(int,input().strip().split()))[:3]

a = numbers[0]
b = numbers[1]
c = numbers[2]

order = [a,b,c]
order.sort()

print(order[0])
print(order[1])
print(order[2])
print()

print(numbers[0])
print(numbers[1])
print(numbers[2])
