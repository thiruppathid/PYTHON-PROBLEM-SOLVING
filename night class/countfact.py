def fac(n):
    if n==1:
        return n
    elif(n==0):
        print("INVALID")
    else:
        return n*fac(n-1)

n=int(input())
a=fac(n)
a=list(str(a))
print(a)
c=0
for i in a[::-1]:
    if i=="0":
        c+=1
    else:
        break
print(c)


