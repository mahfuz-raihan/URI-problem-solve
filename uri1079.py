n = int(input())
result = []
for i in range(0, n):
	num = list(map(float, input().strip().split()))[:3]
	avarage = ((num[0]*2)+(num[1]*3)+(num[2]*5))/10
	result.append(avarage)
	

for i in range(0, n):
	print("%.1f" % result[i])
