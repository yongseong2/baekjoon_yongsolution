N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = []

def dfs(n, s, com):
    global ans
    if n == M:
        ans.append(com)
        return
    prev = 0
    for j in range(s, N):
        if prev != lst[j]:
            prev = lst[j]
            dfs(n+1, j, com + [lst[j]])

dfs(0,0,[])

for x in ans:
    print(*x)