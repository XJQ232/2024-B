n = int( input())
str = input().split()
a=[0]*n
dp=[0]*n
for i in range(n):
    a[i]=int(str[i])
dp[0]=1
max =1
for i in range(1,n):
    curr = 0
    for j in range(i):
        if dp[j]>=curr and a[i]>=a[j]:
            dp[i]=dp[j]+1
            curr = dp[j]
        if max<dp[i]:
            max = dp[i]
print(max)
