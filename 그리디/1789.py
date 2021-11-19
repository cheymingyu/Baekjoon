# 수들의 합

S = int(input())

n = 1
N = 0
while(True):
    N += n
    if (N > S):
        break
    n += 1
    

print(n-1)
