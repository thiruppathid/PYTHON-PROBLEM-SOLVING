def perfect(i):
    #a=int(i**5)
    return int(i**0.5)**2==i
print("ENTER HOW MANY NUMBER")
n=int(input())
lis=list(map(int,input().split()))
per=[]
for i in lis:
    if perfect(i):
        per.append(i)

print(len(per))
print(per)
   #25 77 54 81 48 34     6