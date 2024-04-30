#babad
#bab

str=input()
res=[]
for i in range(len(str)):
    for j in range(i,len(str)):
        a=str[i:j+1]
        if(a==a[::-1]):
            res.append(a)
        else:
            pass
sorted_elemnt=sorted(res,key=len,reverse=True)
print(sorted_elemnt[0])
            
        