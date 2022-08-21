n=int(input())
s=n*(n+1)/2
if s%2:print('NO')
else:
    print('YES')
    s/=2
    a=[]
    b=[]
    while n:
        if s-n>=0:
            a.append(n)
            s-=n
        else:
            b.append(n)
        n-=1
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)