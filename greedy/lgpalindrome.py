n = input()
l = []
st = ""
for i in range(len(n)):
    st += "#" + n[i]
st += "#"
print(st)

for var in range(len(st)):
    c = 0
    i = var - 1
    j = var + 1
    while i >= 0 and j < len(st):
        if st[i] == st[j]:
            pass
        else:
            break
        i -= 1
        j += 1
        c += 1
    l.append([st[var], c])
big= max(l, key=lambda x: x[1])
index = (l.index(big)+1)
count=big[1]
d=""
for i in range(index-count,index+count):
    if st[i]!="#":
        d+="".join(st[i])
print(d)
#
#
#amamracecarhijk