import math
n=int(input())
t=int(math.log(n)/math.log(5))
c=0
for i in range(1,t+1):c+=n//5**i
print(c)
