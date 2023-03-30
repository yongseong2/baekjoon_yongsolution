N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

ans = []
visited = [0]*N

def dfs(n, s, com):
    global ans, visited
    if n == M:
        ans.append(com)
        return
    prev = 0
    for j in range(s, N):
        if visited[j] == 0 and prev != lst[j]:
            prev = lst[j]
            visited[j] = 1
            dfs(n+1, j, com + [lst[j]])
            visited[j] = 0

dfs(0, 0,[])
for x in ans:
    print(*x)