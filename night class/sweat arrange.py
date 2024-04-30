def maxDivide(arr, n):
    lmin = [0 for i in range(n + 1)]
    lmin[n] = float("inf")

    for i in range(n-1, -1, -1):
        lmin[i] = min(lmin[i + 1], arr[i])

    count = 0
    v = -float("inf")
    for i in range(n):
        v = max(v, arr[i])
        if v <= lmin[i + 1]:
            count += 1
    return count
n = int(input())
arr = list(map(int,input().split()))

print(maxDivide(arr, n))