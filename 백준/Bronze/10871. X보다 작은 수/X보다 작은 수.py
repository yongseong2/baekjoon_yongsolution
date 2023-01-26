N,X=map(int,input().split())
A=map(int,input().split())

result=[]
for num in list(A):
    if num<X:
        result.append(num)
        
for i in result:
    print(i,end=' ')