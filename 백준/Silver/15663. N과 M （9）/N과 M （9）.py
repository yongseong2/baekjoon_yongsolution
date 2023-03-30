N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
visited = [0]*N
ans = []

def dfs(n, com):
    global visited, ans
    if n == M:
        ans.append(com)

    prev = 0
    for i in range(N):
        if visited[i] == 0 and prev != lst[i]:
            prev = lst[i]
            visited[i] = 1
            dfs(n+1, com + [lst[i]])
            visited[i] = 0

dfs(0,[])

for x in ans:
    print(*x)