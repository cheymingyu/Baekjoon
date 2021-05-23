# 촌수계산

from collections import deque

def bfs(v, target):
    cnt = 0
    q = deque([[v, cnt]])
    while q:
        value = q.popleft()
        v = value[0]
        cnt = value[1]
        if v == target:
            return cnt
        
        if visit[v] == 0:
            visit[v] = 1
            cnt += 1
            for e in adj[v]:
                if visit[e] == 0:
                    q.append([e, cnt])
    return -1

n = int(input())
a, b = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n+1)]
visit = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

print(bfs(a,b))