#알람시계
H,M=map(int,input().split())
if M<45:
    if H==0:
        H=23
        M=M+60
    else :
        H=H-1
        M=M+60
print(H,M-45)