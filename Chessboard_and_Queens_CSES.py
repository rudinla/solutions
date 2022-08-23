li=[0]*8
c=[1]*8
cc=[1]*15
cp=[1]*15
f=[[1]*8 for _ in range(8)]
for i in range(8):
    s=input()
    for j in range(8):
        if s[j]=='*':f[i][j]=0
count=0
def quay(i):
    for j in range(8):
        if c[j] and cc[i-j+7] and cp[i+j] and f[i][j]:
            li[i]=j
            c[j] = cc[i-j+7] = cp[i+j] = 0
            if i==7:
                global count
                count+=1
            else:quay(i+1)
            c[j] = cc[i-j+7] = cp[i+j] = 1
quay(0)
print(count)
