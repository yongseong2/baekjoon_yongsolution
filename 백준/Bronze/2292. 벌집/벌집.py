#1  ---1
#2-7  ----2
#8-19  ---3
#20-37  ---4
#38-61   --5
#62-    ---6

# 1,6,12,18,24


N=int(input())

# i=0
# s=1
# bulzip=[]
# for i in N:
#     s+=i*6
#     bulzip.append(s)

# for i in range(N):
#     if bulzip[i]<=N<=bulzip[i+1]:
#         print(i+2)

bullzip=1
cnt=1

while N>bullzip:
    bullzip+=6*cnt #벌집이 6의 배수대로 증가
    cnt+=1 #카운트

print(cnt)