word=list(map(str,input().split()))
for i in range(1,len(word)+1):
    print(word[-i],end=' ')
    