N = 10
ans = 0
lst = []
score = 100

for _ in range(N):
    num = int(input())
    lst.append(num)

cnt = 0

for i in range(len(lst)):
    cnt += lst[i]
    if score == cnt:
        ans = cnt
        break
    elif score < cnt:
        if cnt-100 <= abs(cnt-lst[i]-100):
            ans = cnt
            break
        if cnt-100 > abs(cnt-lst[i]-100):
            ans = cnt-lst[i]
            break
    else:
        ans = cnt
        
print(ans)