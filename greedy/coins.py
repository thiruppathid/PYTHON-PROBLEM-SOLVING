denomiation=[1,2,5,10,20,50,100,200,500]
rupee=int(input())
d={}
while rupee:
    for i in reversed(denomiation):
        if rupee>=i :
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            #st.append(i)
            #print(i)
            rupee-=i
            break
    #break
print(d)
            