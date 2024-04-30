def countofdigit(i):
    sum1=0
    while i!=0:
        rem=i%10
        sum1+=rem
        i=int(i//10)
    return sum1


li=list(map(int,input().split()))
for i in li:
    if(0<=i<=9):
        continue
    else:
        a=countofdigit(i)
        print(a,end=" ")

#4 43 345 20 987