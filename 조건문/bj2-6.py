#오븐 시계
H,M=map(int,input().split())
time=int(input())

# if H==23 and M+time>=60:
#     H=0
#     M=M-60
# if M+time>=120:
#     H=H+2
#     M=M-120
# elif M+time>=60:
#     H=H+1
#     M=M-60

# print(H,M+time)

H,M=map(int,input().split())
timer=int(input())

H=H+ timer // 60
M=M+ timer % 60

if M >= 60:
    H += 1
    M=M-60
if H >= 24:
    H=H-24

print(H,M)