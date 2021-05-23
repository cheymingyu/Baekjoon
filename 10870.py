# 피보나치 수 5

n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    f = [0 for _ in range(n+1)]
    f[0] = 0
    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    print(f[n])