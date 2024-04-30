st=[]
arr=[]
lastx,lasty=0,0
for i in range(6):
    li=list(map(int,input().split()))
    st.append(li)
sorted_list = sorted(st, key=lambda x: x[-1])
print(st)
lastx,lasty=sorted_list[0]
arr.append([lastx,lasty])
for x,y in sorted_list[1:]:
    if lasty<x:
        arr.append((x,y))
        lasty=y
print(arr)

        