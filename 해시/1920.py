# 수 찾기

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# dic = {}
# for i in range(N):
#     dic[A[i]] = 1

# for b in B:
#     print(dic.get(b, 0))

for b in B:
    if b in A:
        print(1)
    else:
        print(0)