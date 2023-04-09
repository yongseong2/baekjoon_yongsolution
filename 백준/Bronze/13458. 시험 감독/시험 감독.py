N = int(input())
classes = list(map(int,input().split()))
main, sub = map(int,input().split())

cnt = N
for student in classes:
    student -= main
    if student>0:
        if student%sub:
            cnt += (student//sub) + 1
        else:
            cnt += (student//sub)

print(cnt)