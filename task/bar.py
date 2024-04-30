li=list(map(int,input().split()))
maxi=max(li)
for i in range(len(li)-1):
    mini=min(li[i],li[i+1])
    mini*=2
    if(mini>=maxi):
        maxi=mini
print(maxi)
