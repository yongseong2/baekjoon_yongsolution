from collections import deque

N,M,v = map(int,input().split())
lst = [[]*(M+1) for _ in range(N+1)]

for _ in range(M):
    start, end = map(int,input().split())
    lst[start].append(end)
    lst[end].append(start)

for x in lst:
    x.sort()

def bfs(v):
    visited = [0]*(N+1)
    q = deque([v])
    visited[v] = 1
    ans = []
    while q:
        t = q.popleft()
        ans.append(t)
        for i in lst[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

    return ans

visited = [0]*(N+1)
ans = []
def dfs(lst,v,visited):
    visited[v] = 1
    ans.append(v)
    for i in lst[v]:
        if visited[i] == 0:
            dfs(lst,i,visited)
    return ans


print(*dfs(lst,v,visited))
print(*bfs(v))
