n=int(input())
a=set(map(int,input().split()))
b=set(i for i in range(1,n+1))
print(*(b-a))
