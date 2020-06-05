
alcohol = 0
gasoline = 0
disel = 0
while True:
	n =  int(input())
	if n == 1:
		alcohol +=1
	elif n == 2:
		gasoline += 1
	elif n == 3:
		disel += 1
	elif n == 4:
		break
	else:
		continue

print("MUITO OBRIGADO")
print("Alcool: {}".format(alcohol))
print("Gasolina: {}".format(gasoline))
print("Diesel: {}".format(disel))
