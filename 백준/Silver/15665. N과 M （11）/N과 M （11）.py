N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
ans = []

def dfs(n, com):
    global ans
    if n == M:
        ans.append(com)
        return

    prev = 0
    for j in range(N):
        if prev != lst[j]:
            prev = lst[j]
            dfs(n+1, com + [lst[j]])

dfs(0, [])

for x in ans:
    print(*x)