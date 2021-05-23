# 1,2,3 더하기

T = int(input())
test = list(int(input()) for _ in range(T))

result = [0, 1, 2, 4]

def count_way(n):
    if len(result) == n:
        result.append(sum(result[n-3:n]))
    else:
        count_way(n-1)
        result.append(sum(result[n-3:n]))


for i in range(T):
    n = test[i]
    if len(result) < n+1:
        count_way(n)

    print(result[n])
