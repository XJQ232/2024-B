from math import isqrt
n = int(input())
ans=[]
def check(a):
    global ans
    is_prime[0]=is_prime[1]=1
    for i in range(2,a+1):
        if is_prime[i] == 0: 
            if i**2 <= m:
                ans.append(i**2) 
        for j in range(i*i,a+1,i):
            is_prime[j]=1
l1=list(map(int,input().split()))
m = max(l1)
is_prime=[0]*(isqrt(m)+2)
check(isqrt(m)+1)
for i in l1:
    if i in ans:
        print("YES")
    else:
        print("NO")