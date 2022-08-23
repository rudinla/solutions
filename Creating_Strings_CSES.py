s=input()
cc=[0]*26
c=0
for i in s:cc[ord(i)-ord('a')]+=1
l=len(s)
def gt(n):
    kq=1
    for i in range(2,n+1):kq*=i
    return kq
li=[0]*l
def quay(diem):
    for i in range(26):
        if cc[i]:
            cc[i]-=1
            li[diem]=chr(ord('a')+i)
            if diem==l-1:print(''.join(li))
            else:quay(diem+1)
            cc[i]+=1
se=set(s)
kqua=gt(l)
for i in se:kqua/=gt(s.count(i))
print(int(kqua))
quay(0)
