N = float(input())


print("NOTAS:")
if(N >= 100):
	print("{} nota(s) de R$ 100.00".format(int(N/100)))
else:
	print("0 nota(s) de R$ 100.00")
aux = N % 100
if(aux >= 50):
	print("{} nota(s) de R$ 50.00".format(int(aux/50)))
else:
	print("0 nota(s) de R$ 50.00")
aux = aux % 50
if(aux >= 20):
	print("{} nota(s) de R$ 20.00".format(int(aux/20)))
else:
	print("0 nota(s) de R$ 20.00")
aux = aux % 20
if(aux >= 10):
	print("{} nota(s) de R$ 10.00".format(int(aux/10)))
else:
	print("0 nota(s) de R$ 10.00")
aux = aux % 10
if(aux >= 5):
	print("{} nota(s) de R$ 5.00".format(int(aux/5)))
else:
	print("0 nota(s) de R$ 5.00")
aux = aux % 5
if(aux >= 2):
	print("{} nota(s) de R$ 2.00".format(int(aux/2)))
else:
	print("0 nota(s) de R$ 2.00")
aux = aux % 2
print("MOEDAS:")
if(aux >= 1):
	print("{} moeda(s) de R$ 1.00".format(int(aux/1)))
else:
	print("0 moeda(s) de R$ 1.00")
aux = aux % 1
if(aux >= 0.5):
	print("{} moeda(s) de R$ 0.50".format(int(aux/0.5)))
else:
	print("0 moeda(s) de R$ 0.50")
aux = aux % 0.5
if(aux >= 0.25):
	print("{} moeda(s) de R$ 0.25".format(int(aux/0.25)))
else:
	print("0 moeda(s) de R$ 0.25")
aux = aux % 0.25
if(aux >= 0.1):
	print("{} moeda(s) de R$ 0.10".format(int(aux/0.1)))
else:
	print("0 moeda(s) de R$ 0.10")
aux = aux % 0.1
if(aux >= 0.05):
	print("{} moeda(s) de R$ 0.05".format(int(aux/0.05)))
else:
	print("0 moeda(s) de R$ 0.05")
aux = aux % 0.05
if(aux >= 0.01):
	print("{} moeda(s) de R$ 0.01".format(int(aux/0.01)))
else:
	print("0 moeda(s) de R$ 0.01")
