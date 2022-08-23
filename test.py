n=int(input())
li=list(map(int,input().split()))
def solve(i,s1,s2):
    if i==n:return abs(s1-s2)
    return min(solve(i+1,s1+li[i],s2),solve(i+1,s1,s2+li[i]))
print(solve(0,0,0))