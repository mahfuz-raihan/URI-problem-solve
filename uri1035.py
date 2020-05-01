values = list(map(int, input().strip().split()))

if((values[1]>values[2]) & (values[3]> values[0])):
    if((values[2]+values[3])>(values[0]+values[1])):
        if((values[2]>0) & (values[3]>0)):
            if(values[0]%2==0):
                print("Valores aceitos")
else:
    print("Valores noa aceitos")
