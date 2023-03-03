N, K = map(int, input().split())

female = [0] * (7)
male = [0] * (7)

for _ in range(N):
    s, grade = map(int, input().split())

    if s == 0:
        female[grade] += 1

    if s == 1:
        male[grade] += 1

cnt = 0
for room in female:
    if 0< room <= K:
        cnt += 1
    elif room > K:
        n = room//K + 1
        cnt += n

for room in male:
    if 0< room <= K:
        cnt += 1
    elif room > K:
        n = room//K + 1
        cnt += n

print(cnt)
