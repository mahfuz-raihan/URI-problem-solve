n = int(input())

n1 = 1
n2 = 2
n3 = 3
print("{0} {1} {2} PUM".format(n1, n2, n3))
for i in range(1,n):
    n1 += 4
    n2 += 4
    n3 += 4
    print("{0} {1} {2} PUM".format(n1, n2, n3))
