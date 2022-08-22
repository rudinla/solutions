for _ in range(int(input())):
    a,b=map(int,input().split())
    if (a+b)%3==0 and max(a,b)<=min(a,b)*2:print('YES')
    else:print('NO')
