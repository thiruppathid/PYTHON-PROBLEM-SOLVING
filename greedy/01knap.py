w = 8
n = 4
wt = [3, 4, 6, 5]
pf = [2, 3, 1, 4]

d = {}
for i in range(len(wt)):
    d[wt[i]] = pf[i]

d = sorted(d.items(), key=lambda x: x[0])
print(d)

mat = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

print("Initial matrix:")
for row in mat:
    print(row)

for i in range(1, n + 1):
    for j in range(1, w + 1):
        if wt[i - 1] <= j:
            mat[i][j] = max(mat[i - 1][j], pf[i - 1] + mat[i - 1][j - wt[i - 1]])
        else:
            mat[i][j] = mat[i - 1][j]

for row in mat:
    print(row)

print("Maximum profit:", mat[n][w])
