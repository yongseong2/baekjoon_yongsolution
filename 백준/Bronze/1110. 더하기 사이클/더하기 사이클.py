N=int(input())
num=N
cnt=0

while True:
    a=num//10
    b=num%10
    c=b*10+(a+b)%10
    cnt+=1
    num=c
    if c==N:
        print(cnt)
        break