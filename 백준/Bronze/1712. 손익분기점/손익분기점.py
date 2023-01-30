A,B,C=map(int,input().split())

# cnt=0

# while True:
#     cnt+=1
#     if (C-B)<=0:
#         cnt=-1
#         print(cnt)
#         break
#     if (A+B*cnt)<(C*cnt):
#         print(cnt)


if B>=C:
    print(-1)
else:
    print(A//(C-B)+1)