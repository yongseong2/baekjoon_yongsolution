def dfs(n, s, com):
    global ans
    if n == 6:
        ans.append(com)
    for i in range(s, N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1, i, com + [lst[i]])
            visited[i] = 0





while True:
    N, *lst = map(int,input().split())
    lst = list(lst)
    ans = []
    visited = [0]*N
    dfs(0, 0, [])

    for x in ans:
        print(*x)
    print()

    if N == 0:
        break
