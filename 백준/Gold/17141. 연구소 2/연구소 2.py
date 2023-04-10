from collections import deque
from itertools import combinations
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

answer = float("inf")

def bfs(v):
    q = deque(v)
    visited = [[-1]*N for _ in range(N)]
    cnt = 0
    for i, j in q:
        visited[i][j] = 0

    while q:
        ci, cj = q.popleft()
        for di, dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni, nj = ci+di, cj + dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == -1 and arr[ni][nj] != 1:
                q.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1
                cnt = max(cnt, visited[ni][nj])

    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and arr[i][j] != 1:
                return float("inf")
    return cnt

virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append((i,j))

for v in combinations(virus, M):
    answer = min(bfs(v),answer)

if answer == float("inf"):
    print(-1)
else:
    print(answer)