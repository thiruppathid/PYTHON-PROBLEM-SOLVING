n=int(input())#6
li=list(map(int,input().split())) # 3 2 1 4 5 6
org=li
dup=sorted(li)
ind=1
part=[]
while (len(org))>0:
    if sorted(org[:ind])==dup[:ind]:
        part.append(dup[:ind])
        org=org[ind:]
        dup=dup[ind:]
        ind=1
    else:
        ind+=1
print(part)
