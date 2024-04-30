m = input()  
a = list(m)  
m = int(m)   


closest_permutation = m
min_diff = float('inf')


for i in range(len(a) - 1):
    
    a[i], a[i+1] = a[i+1], a[i]
    
    
    b = int(''.join(a))
    
 
    diff = b - m
    if 0 < diff < min_diff :
        min_diff = diff
        closest_permutation = b
    
    a[i], a[i+1] = a[i+1], a[i]
print(closest_permutation)
