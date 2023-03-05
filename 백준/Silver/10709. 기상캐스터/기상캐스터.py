H, W = map(int,input().split())
arr = [["."]+list(input())+["."] for _ in range(H)]

for lst in arr:
    cnt = 0
    for i in range(len(lst)):
        if lst[i] == 'c':
            for j in range(i, len(lst)-1):
                lst[j] = cnt
                cnt += 1
                if lst[j+1] == 'c':
                    cnt = 0
                    break
        if lst[i] == '.':
            lst[i] = -1

for result in arr:
    ans = result[1:W+1]
    print(*ans)