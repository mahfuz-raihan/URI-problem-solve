n = int(input())
rabbit = 0
rat = 0
frog = 0

for i in range(0, n):
	animal = input().split()
	amount = int(animal[0])
	short_form = str(animal[1])
	if short_form == 'C':
		rabbit += amount
	elif short_form == 'R':
		rat += amount
	elif short_form == 'S':
		frog += amount

total = rabbit+rat+frog
p_rabbit= float(100*(rabbit/total))
p_rat = float(100*(rat/total))
p_frog = float(100*(frog/total))

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(rabbit))
print("Total de ratos: {}".format(rat))
print("Total de sapos: {}".format(frog))
print("Percentual de coelhos: {0:.2f} {1}".format(p_rabbit, "%"))
print("Percentual de ratos: {0:.2f} {1}".format(p_rat, "%"))
print("Percentual de sapos: {0:.2f} {1}".format(p_frog, "%"))
	
