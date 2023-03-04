N = int(input())
for _ in range(N):
    na,*A = list(map(int,input().split()))
    nb,*B = list(map(int,input().split()))

    acnt_lst = [0] * 5
    bcnt_lst = [0] * 5
    ans = 'D'

    for i in range(na):
        if A[i] == 4:
            acnt_lst[4] += 1
        if A[i] == 3:
            acnt_lst[3] += 1
        if A[i] == 2:
            acnt_lst[2] += 1
        if A[i] == 1:
            acnt_lst[1] += 1

    for i in range(nb):
        if B[i] == 4:
            bcnt_lst[4] += 1
        if B[i] == 3:
            bcnt_lst[3] += 1
        if B[i] == 2:
            bcnt_lst[2] += 1
        if B[i] == 1:
            bcnt_lst[1] += 1

    for i in range(4,0,-1):
        if acnt_lst[4] > bcnt_lst[4]:
            ans = 'A'
            break
        if acnt_lst[4] < bcnt_lst[4]:
            ans = 'B'
            break
        else:
            if acnt_lst[3] > bcnt_lst[3]:
                ans = 'A'
                break
            if acnt_lst[3] < bcnt_lst[3]:
                ans = 'B'
                break
            else:
                if acnt_lst[2] > bcnt_lst[2]:
                    ans = 'A'
                    break
                if acnt_lst[2] < bcnt_lst[2]:
                    ans = 'B'
                    break
                else:
                    if acnt_lst[1] > bcnt_lst[1]:
                        ans = 'A'
                        break
                    if acnt_lst[1] < bcnt_lst[1]:
                        ans = 'B'
                        break


    print(ans)