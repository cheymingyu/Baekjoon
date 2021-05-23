# 1로 만들기

def make_one(n):
    memo[0] = 0
    memo[1] = 0
    memo[2] = 1
    memo[3] = 1

    for i in range(4, n+1):
        memo[i] = memo[i-1] + 1

        if i % 2 == 0 and memo[i] > memo[i//2] + 1:
            memo[i] = memo[i//2] + 1

        if i % 3 == 0 and memo[i] > memo[i//3] + 1:
            memo[i] = memo[i//3] + 1

    return memo[n]


if __name__ == '__main__':
    n = int(input())
    memo = [0 for i in range(n+4)]
    print(make_one(n))
