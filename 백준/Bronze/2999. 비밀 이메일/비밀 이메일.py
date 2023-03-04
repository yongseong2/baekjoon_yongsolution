word = input()
N = len(word)


R = C = 0
for r in range(N+1):
    for c in range(r,N+1):
        if 0<r<=N and 0<c<=N and r*c == N and r<=c :
            if R < r:
                R = r
                C = c

arr = [['']*C for _ in range(R)]

cnt = 0
for j in range(C):
    for i in range(R):
        arr[i][j] = word[cnt]
        cnt += 1


for lst in arr:
    for ans in lst:
        print(ans,end='')