n,k=map(int,input().split())
li=list(map(int,input().split()))
st=[]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        sub=li[i:j]
        if sum(sub)==k:
            st.append([i+1,j])

print(*st)
#10 15
#5 3 7 14 18 1 18 4 8 3
            
        