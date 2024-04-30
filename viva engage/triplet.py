'''from itertools import combinations
lis=list(map(int,input().split()))
li=combinations(lis,3)
d=[]
c=0
for i in li:
    i=list(i)
    #print(i,end=" ")
    a=sorted(i)
    if a in d:
        continue
    else:
        if(sum(a)==0):
            c+=1
            d.append(a)
        else:
            d.append(a)'''
lis = list(map(int, input().split()))
n = len(lis)
c = 0

# Convert the list to a set for constant time lookups
lis_set = set(lis)

# Iterate through all possible pairs of elements
for i in range(n):
    for j in range(i + 1, n):
        # Calculate the complement needed to make the sum zero
        complement = -(lis[i] + lis[j])
        # Check if the complement exists in the set and is not one of the original elements
        if complement in lis_set and complement != lis[i] and complement != lis[j]:
            c += 1

# Divide the count by 3 to account for permutations of the same triplet
print(c // 3)

#print(c)
#0 -1 2 -3 1 -2