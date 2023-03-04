lst = list(map(int,input().split()))

N = len(lst)
ans = sorted(lst)

while lst != ans:
    for i in range(1,N):
        if lst[i-1]>lst[i]:
            lst[i-1],lst[i] = lst[i],lst[i-1]
            print(*lst)