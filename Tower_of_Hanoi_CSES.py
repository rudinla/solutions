n=int(input())
print(2**n-1)
def xuat(a,b):
    print(a,b)
def thap(t,a,b,c):
    if t==1:xuat(a,c)
    else:
        thap(t-1,a,c,b)
        xuat(a,c)
        thap(t-1,b,a,c)
thap(n,1,2,3)
