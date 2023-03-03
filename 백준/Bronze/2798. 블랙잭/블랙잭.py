N, M = map(int,input().split())
lst = list(map(int,input().split()))

ans = 9999999
res = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sm =lst[i]+lst[j]+lst[k]
            if sm <= M:
                min = abs(sm-M)
                if ans>min:
                    ans = min
                    res = sm

print(res)