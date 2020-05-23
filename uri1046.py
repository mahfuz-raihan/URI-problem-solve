time = list(map(int, input().strip().split()))[:2]

start_time = time[0]
end_time = time[1]

duration_time = end_time - start_time
if (duration_time < 0):
    duration = 24 + duration_time
    print("O JOGO DUROU %d HORA(S)" % duration)
elif(start_time == end_time):
    print("O JOGO DUROU 24 HORA(S)")
else:
    print("O JOGO DUROU %d HORA(S)" %duration_time)
