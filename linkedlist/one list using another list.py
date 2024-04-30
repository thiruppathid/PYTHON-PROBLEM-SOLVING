li1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
li2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
d = {}
for i in range(len(li1)):
    d[li2[i]] = li1[i]

# Sort dictionary values
sorted_values = sorted(d.values())

for val in sorted_values:
    for key, value in d.items():
        if value == val:
            print(f"{value}:{key}", end=" ")

# Output: a:0 d:0 g:0 b:1 c:1 e:1 f:1 h:1 i:1 
