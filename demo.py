n=int(input())
print(0)
for i in range(2,n+1):
    t=i*i
    print(int(t*(t-1)/2-(4*(i-2)*(i-1))))