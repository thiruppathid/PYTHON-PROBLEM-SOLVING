n=int(input())
li=list(map(int,input().split()))
c=1
maxi=li[0]
for i in range(1,n):
    if(maxi<li[i]):
        c+=1
        maxi=li[i]
print(c)