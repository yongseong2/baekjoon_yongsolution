C = int(input())
N = int(input())

ans1_lst = []
max_ = 0
ans1 = 0
ans2 = 0

lst = [0]*(C+1)

for i in range(N):
    P, K = map(int,input().split())

    ans1_lst.append(K-P)

    for j in range(P,K+1): # 케이크 리스트
        if not lst[j]:
            lst[j] = i+1

for i in range(len(ans1_lst)): # ans1 가장 많을거 같은 예상되는 사람
    if max_ < ans1_lst[i]:
        max_ = ans1_lst[i]
        ans1 = i+1

ans2_lst = [x for x in lst if x]

max_cnt = 0
for i in range(len(ans2_lst)): #ans2 실제로 가장 많은 사람
    if max_cnt < ans2_lst.count(i):
        max_cnt = ans2_lst.count(i)
        ans2 = i

print(ans1)
print(ans2)