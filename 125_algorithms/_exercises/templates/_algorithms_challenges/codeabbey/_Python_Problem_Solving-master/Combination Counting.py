___  fact(n
    __ n __ 0:
        r_ 1
    res = 1
    for i in range(n,0,-1
        res = res * i
    r_ res
for i in range(int(input())):
    n,k = list(map(int,input().split()))
    result = 0
    result = fact(n) / (fact(k) * fact(n-k))
    print(int(result),end=' ')