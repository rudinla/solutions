s=input()
dem=0
se=set(s)
if len(se)==1:
    print(s)
    exit()
chuoi=''
l=len(s)
for i in se:
    c=s.count(i)
    if c%2:
        t=i*c
        dem+=1
        if dem>1 or l%2==0:
            print('NO SOLUTION')
            exit()
    else:chuoi+=i*(c//2)
if l%2:chuoi+=t+chuoi[::-1]
else:chuoi+=chuoi[::-1]
print(chuoi)
