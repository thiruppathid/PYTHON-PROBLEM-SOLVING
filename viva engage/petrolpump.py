n=int(input())
petrolpum=list(map(int,input().split()))
petrol=list(map(int,input().split()))
for i in range(len(petrolpum)):
    if(n>petrolpum[i]):
        n=n-petrolpum[i]+petrol[i]
    else:
        print(abs(n-petrolpum[i]))
        break
if(i==len(petrolpum)):
    print(n)

