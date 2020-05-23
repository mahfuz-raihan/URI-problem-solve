values = list(map(int, input().strip().split()))[:2]
a = values[0]
b = values[1]

if(b % a == 0 or a % b == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
