n=int(input("NUMBER OF ROWS"))
st=[]
for i in range(n):
    st.append([0]*n)
    
def vertexadd(v,u):
    st[v][u]=1
    st[u][v]=1

vertexadd(0,1)
vertexadd(0,2)
vertexadd(0,3)
for i in st:
    print(*i)


if contains_cycle:
    print("yes")
else:
    print("no")