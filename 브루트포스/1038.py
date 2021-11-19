# 감소하는 수

from itertools import combinations

N = int(input())
dec = list()

for i in range(1, 11):
    for comb in combinations(range(10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        dec.append(int("".join(map(str, comb))))

dec.sort()

if len(dec) > N:
    print(dec[N])
else:
    print(-1)

# 출처:https://ryu-e.tistory.com/59