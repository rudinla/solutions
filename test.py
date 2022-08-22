n=int(input())
li=['']
for i in range(n):
    l=len(li)
    for j in range(l-1,-1,-1):li.append(li[j])
    l*=2
    for j in range(l):
        if j<l/2:li[j]+='0'
        else:li[j]+='1'
for i in range(l):
    print(li[i])