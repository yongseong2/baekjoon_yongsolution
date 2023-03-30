N, M = map(int,input().split())
lst = list(map(int,input().split()))
ans = []
lst.sort()
visited = [0]*N

def dfs(n, com):
    global ans
    if n == M:
        ans.append(com)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1, com + [lst[i]])
            visited[i] = 0



dfs(0,[])

for x in ans:
    print(*x)