def calculation():
	while True:
		count = 0
		score = 0
		while count < 2:
			number = float(input())
			if 0 <= number and number <= 10:
				count += 1
				score += number
			else:
				print("nota invalida")
		print("media = {0:.2f}".format(score/2))
		break
if __name__	== "__main__":
	calculation()
	x = 3
	while (x != 1 or x != 2):
		x = int(input())
		print("novo calculo (1-sim 2-nao)")
		if x == 1:
			calculation()
		elif(x == 2):
			break
		else:
			continue
