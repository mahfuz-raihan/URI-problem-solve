day1 = input().split()
d1 = int(day1[1])

time = list(map(int, input().split(" : ")))
hour1 = time[0]
minutes1 = time[1]
second1 = time[2]

day2 = input().split()
d2 = int(day2[1])

time1 = list(map(int, input().split(" : ")))
hour2 = time1[0]
minutes2 = time1[1]
second2 = time1[2]

day = d2 - d1

hour = hour2 - hour1
if(hour < 0):
	hour = 24 + hour
	day -= 1

minutes = minutes2 - minutes1 
if(minutes < 0):
	minutes = 60 + minutes
	hour = hour -1

second = second2 - second1
if(second < 0):
	second = 60 + second
	minutes = minutes - 1
if day <= 0:
	day = 0
	
print("%d dia(s)" % day)
print("%d hora(s)" % hour)
print("%d minuto(s)" % minutes)
print("%d segundo(s)" % second)
