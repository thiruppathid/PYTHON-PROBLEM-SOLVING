def prefix(st):
    initial=st[0]
    res=''
    for i in range(len(initial)):
        for s in st[1:]:
            if(i==len(s) or s[i]!=st[0][i]):
                return res
        res+=st[0][i]
    print(res)
lis=list(map(str,input().split()))
prefix(lis)