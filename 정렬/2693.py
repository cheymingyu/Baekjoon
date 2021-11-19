# N번째 큰수

N = int(input())

test = [list(map(int, input().split())) for _ in range(N)]

for l in test:
    l.sort(reverse=True)
    print(l[2])