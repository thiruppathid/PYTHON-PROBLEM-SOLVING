n=int(input())
li=list(map(int,input().split()))
c=0
st=[]
for i in range(len(li)):
    c=0
    for j in range(i+1,len(li)):
        if(li[i]>li[j]):
            c+=1
    st.append(c)
print(*st)
#6 4 2 1 5