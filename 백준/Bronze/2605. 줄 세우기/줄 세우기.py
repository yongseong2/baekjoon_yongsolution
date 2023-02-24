N = int(input())
lst = list(map(int,input().split()))

stu = [x for x in range(1,N+1)]

for i in range(N):
    for j in range(lst[i]):
        stu[i],stu[i-1] = stu[i-1],stu[i]
        i = i - 1

print(*stu)
