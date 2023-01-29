T=int(input())
for i in range(T):
    R, S=input().split()

    result=''
    for abc in S:
        result+=abc*int(R)
        
    print(result)