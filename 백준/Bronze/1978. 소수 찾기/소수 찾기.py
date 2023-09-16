N = int(input())
nums = list(map(int, input().split()))

ans = 0

for num in nums:
    error = False
    if num > 1:
        for i in range(2, num):
            if num%i==0:
                error =True
        if error == False:
            ans += 1


print(ans)