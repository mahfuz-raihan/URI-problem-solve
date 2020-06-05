import math

count = 0
inter_win = 0
germio_win = 0
match_draw = 0
team1 = 'Inter'
team2 = 'Germio'

while True:
	inter_goal, germio_goal = list(map(int, input().strip().split()))
	choice = int(input("Novo grenal (1-sim 2-nao)\n"))
	count += 1
	if inter_goal > germio_goal:
		inter_win +=1
	elif inter_goal == germio_goal:
		match_draw += 1
	elif inter_goal < germio_goal:
		germio_win += 1
	
	if choice == 1:
		continue
	else:
		break
		
print("{} grenais".format(count))
print("Inter:{}".format(inter_win))
print("Gremio:{}".format(germio_win))
print("Empates:{}".format(match_draw))
if inter_win > germio_win:
	print("{} venceu mais".format(team1))
elif inter_win < germio_win:
	print("{} venceu mais".format(team2))
elif inter_win == germio_win:
	print("Não houve vencedor")
