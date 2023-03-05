N = 5

B = [list(map(int,input().split())) for _ in range(N)]
arr = [list(map(int,input().split())) for _ in range(N)]

call = []

for i in range(N):
    for j in range(N):
        call.append(arr[i][j])

ans = 0
for x in call:
    ans += 1
    sm = 0
    sm_t = 0
    cnt = 0
    for r in range(N):
        for c in range(N):
            if B[r][c] == x:
                B[r][c] = 0
                break
    for lst in B:
        if sum(lst) == 0:
            cnt += 1
    B_t = list(map(list, zip(*B)))
    for lstt in B_t:
        if sum(lstt) == 0:
            cnt += 1
    for k in range(N):
        sm += B[k][k]
        sm_t += B[k][N-k-1]
    if sm == 0:
        cnt += 1
    if sm_t == 0:
        cnt += 1
    if cnt >= 3:
        break

print(ans)