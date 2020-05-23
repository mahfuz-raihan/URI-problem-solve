""" this solution seems wrong in IRI OJ, but every logic is clear.
please check another solution and fix it. and drop a solution in comment.
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

even_count = odd_count = positive_count = negative_count = 0

for i in (a, b, c, d, e):
	if (abs(i) % 2 == 0):
		even_count += 1
	if (i % 2 != 0):
		odd_count += 1
	if (i > 0):
		positive_count +=1
	if (i < 0):
		negative_count += 1

print("%d valor(es) par(es)" % even_count)
print("%d valor(es) impar(es)" % odd_count)
print("%d valor(es) positivo(s)" % positive_count)
print("%d valor(es) negativo(es)" % negative_count)
