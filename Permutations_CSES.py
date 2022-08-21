n=int(input())
if n==1:print(1)
elif n<4:print('NO SOLUTION')
else:
    a=[i for i in range(1,n+1,2)]
    b=[i for i in range(2,n+1,2)]
    print(*(b+a))
