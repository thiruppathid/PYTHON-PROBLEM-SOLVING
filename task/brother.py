# 321   321
#2345  2354
#85734  84753
m = int(input())
a = [int(d) for d in str(m)]
diff=99999
st=[]
for i in range(len(a)-1,0,-1):
    a[i],a[i-1]=a[i-1],a[i]
    b= int(''.join(map(str, a)))
    if(b-m)>0:
        if diff>b-m:
            diff=b-m
            if st:
                st.pop()
                st.append(b)
            else:
                st.append(b)
            a=[int(d) for d in str(m)]
        elif(b-m)<0:
            a=[int(d) for d in str(m)]
            continue
if st==0:
    print(m)
else:
    print(st.pop())
            
        