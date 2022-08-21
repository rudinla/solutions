for _ in range(int(input())):
    a,b=map(int,input().split())
    maxx=max(a,b)
    t=(maxx-1)**2
    if t%2:t+=maxx+a-b
    else:t+=maxx+b-a
    print(t)