A,B,V=map(int,input().split())

#시간초과
# v=V
# one_day=A-B
# day=0

# while True:
#     v=v-one_day
#     day+=1
#     if A>=v:
#         day+=1
#         print(day)
#         break

k=(V-B)/(A-B)

if k==int(k):
    print(int(k))
    
else:
    print(int(k)+1)