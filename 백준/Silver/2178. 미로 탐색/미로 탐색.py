from collections import deque

def bfs(si,sj):
    visited = [[0]*M for _ in range(N)]
    visited[si][sj] = 1
    q= deque([(si,sj)])

    while q:
        i,j = q.popleft()
        for di, dj in ((0,1),(1,0),(-1,0),(0,-1)):
            ni,nj = i+di, j +dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj]==0:
                if arr[ni][nj] == 1:
                    q.append((ni,nj))
                    visited[ni][nj] = visited[i][j] + 1

    return visited[N-1][M-1]

N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]

print(bfs(0,0))