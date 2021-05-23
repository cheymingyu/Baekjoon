N = int(input())
new = 0

a = N // 10
b = N % 10
tmp = a+b
cycle = 0
if N == 0:
    print(1)
else:
    while new != N:
        new_b = tmp % 10
        new = b*10 + new_b
        a = new // 10
        b = new % 10
        tmp = a+b
        cycle += 1

    print(cycle)
