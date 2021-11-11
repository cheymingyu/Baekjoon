# 정수 삼각형

# 삼각형 크기 입력
n = int(input())

# 삼각형 입력
tri = [list(map(int, input().split())) for _ in range(n)]

# dp 진행할 삼각형 복사
dp = tri.copy()

# 삼각형 아래서부터 올라오면서 바로 아래 두개의 수 중 
# 큰 수를 현재 수에 더함
for i in range(len(dp)-2, -1, -1):
    for j in range(len(dp[i])):
        max_val = max(dp[i+1][j], dp[i+1][j+1])
        dp[i][j] += max_val
        
print(dp[0][0])