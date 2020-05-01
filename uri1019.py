import time 
  
def convert(seconds): 
    return time.strftime("%H:%M:%S", time.gmtime(N)) 
      
# Driver program 
N = int(input())
print(convert(N)) 
