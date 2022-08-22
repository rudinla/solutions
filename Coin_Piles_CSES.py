for _ in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        k=a-b
        a-=2*k
        b-=k
        if a==b and a>=0 and a%3==0:print('YES')
        else:print('NO')
    else:
        k=b-a
        b-=2*k
        a-=k
        if a==b and a>=0 and a%3==0:print('YES')
        else:print('NO')
