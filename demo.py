s=input()
c=1
li=[]
for i in range(len(s)):
    if i==len(s)-1:
        li.append(c)
    elif s[i]==s[i+1]:
        c+=1
    else:
        li.append(c)
        c=1
print(max(li))