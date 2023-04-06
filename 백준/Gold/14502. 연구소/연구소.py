from collections import deque
import copy

def bfs():
    global ans
    q = deque()
    visited = copy.deepcopy(arr)

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 2:
                q.append((i, j))

    while q:
        ci, cj = q.popleft()
        for di, dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni, nj = ci + di, cj +dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0:
                visited[ni][nj] = 2
                q.append((ni, nj))

    cnt = 0
    for i in range(N):
        cnt += visited[i].count(0)

    return cnt


def dfs(n):
    global ans
    if n == 3:
        ans = max(ans, bfs())
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(n+1)
                arr[i][j] = 0

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

ans = 0
dfs(0)

print(ans)