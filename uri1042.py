x,y,z = input().split()

j = x
k = y
l = z

a = int(x)
b = int(y)
c = int(z)

if a > b and a > c:
    big = a
if a < b and b > c:
    big = b
if c > a and c > b:
    big = c

if a < b and a < c:
    small = a
if b < a and b < c:
    small = b
if c < a and c < b:
    small = c

if big == a and small == b:
    middle = c
if big == b and small == a:
    middle = c
if big == b and small == c:
    middle = a
if big == c and small == b:
    middle = a

if big == a and samll == c:
    middle == b
if big == c and small == a:
    middle = b
    
print(small)
print(middle)
print(big)

print()

print(j)
print(k)
print(l)
