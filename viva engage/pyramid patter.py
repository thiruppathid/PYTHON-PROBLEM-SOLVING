def pyramid(res):
    n=len(res)
    if(n==1 or n==0):
        print(res)
    else:
        initial=res[0]
        for i in range(0,len(initial)+1):
            c=0
            for j in res[1:n]:
                if(c==0):
                    a=initial[:i]+j[:i]
                    c=1
                else:
                    a+=j[:i]
            print(a)
        print("")
str=input()
res=""
for i in str:
    if i.isupper():
        res+='&'+i
    else:
        res+=i
        
res=res.split("&")
res=res[1:]
pyramid(res)