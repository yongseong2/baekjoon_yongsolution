T=int(input())
for tc in range(1,T+1):
    H,W,N=map(int,input().split())

    height=0
    way=0
    height=N%H
    way=N//H
    
    if N%H==0:

        height+=H
        way-=1
    
    # lst=[]
    # if way<10:
    #     lst=[height,0,way+1]
    
    # else:
    #     lst=[height,way+1]
    
    # result=''.join(map(str,lst))
    
    print(f'{height*100+way+1}')