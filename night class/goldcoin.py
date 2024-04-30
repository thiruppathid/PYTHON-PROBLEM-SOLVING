n,k=map(int,input().split())
li=list(map(int,input().split()))
st=[]
for i in range(len(li)):
    for j in range(i,len(li)-1):
        sub=li[i:j+1]
        if sum(sub)==k:
            st.append([i+1,j+1])
            continue
for i in st:
    print(*i)
#10 15
#5 3 7 14 18 1 18 4 8 3
            
        