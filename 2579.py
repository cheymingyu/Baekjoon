# 계단 오르기

n = int(input())
s = [int(input()) for _ in range(n)]
dp = []

if n == 0:
    dp.append(0)
elif n == 1:
    dp.append(s[0])
elif n == 2:
    dp.append(s[0])
    dp.append(s[0]+s[1])
elif n >= 3:
    dp.append(s[0])
    dp.append(s[0]+s[1])
    dp.append(max(s[1]+s[2], s[0]+s[2]))

    for i in range(3,n):
        dp.append(max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i]))

print(dp.pop())