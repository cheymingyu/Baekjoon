# 부분합

N, S = map(int, input().split())

seq = list(map(int, input().split()))

left = 0
right = 0

min_len = N+1
temp = 0

while(True):
    if temp >= S:
        min_len = min(min_len, right - left)
        temp -= seq[left]
        left += 1
    elif right == N:
        break
    else:
        temp += seq[right]
        right += 1

if min_len == N+1:
    print(0)
else:
    print(min_len)
