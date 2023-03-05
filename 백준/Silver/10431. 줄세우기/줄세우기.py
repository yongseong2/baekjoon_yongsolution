N = int(input())
for _ in range(N):
    n, *lst = map(int, input().split())

    cnt = 0
    for i in range(1, len(lst)):
        for j in range(i-1,-1,-1):
            if lst[i] < lst[j]:
                cnt += 1
                lst[i],lst[j] = lst[j], lst[i]
                i = i-1

    print(n, cnt)
