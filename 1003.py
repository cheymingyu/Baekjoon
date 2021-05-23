# 피보나치 함수

T = int(input())
N = list(int(input()) for _ in range(T))

result = [0 for _ in range(T)]

dp = [[0 for _ in range(2)] for _ in range(max(N)+1)]

dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, max(N)+1):
    dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]

for i in range(T):
    result[i] = dp[N[i]]

for i in range(T):
    print("%d %d"%(result[i][0], result[i][1]))
