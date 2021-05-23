# 토마토

import sys
from collections import deque
        
M, N, H = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N*H)]

visit = [[0]*M for _ in range(N*H)]

dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [N,-N,0,0,0,0]

cnt = 0

vertex = deque()
for i in range(N*H):
    for j in range(M):
        if matrix[i][j] == 1:
            visit[i][j] = 1
            vertex.append([i,j])
        elif matrix[i][j] == -1:
            visit[i][j] = -1

def bfs(v):
    global cnt
    q = v
    temp = deque()

    while q or temp:
        while q:
            tomato = q.popleft()
            x = tomato[0]
            y = tomato[1]
            for i in range(6):
                nx, ny = x + dx[i] + dz[i], y + dy[i]
                if 0 <= nx < N*H and 0 <= ny < M:
                    if x-nx == 1 and (x+1)%N == 1:
                        pass
                    elif nx-x == 1 and (x+1)%N == 0:
                        pass
                    else:
                        if matrix[nx][ny] == 0 and visit[nx][ny] == 0:
                            matrix[nx][ny] = 1
                            visit[nx][ny] = 1
                            temp.append([nx,ny])
                        elif matrix[nx][ny] == -1:
                            visit[nx][ny] = -1
        cnt += 1
        for i in visit:
            print(i)
        print()
        while temp:
            q.append(temp.popleft())

bfs(vertex)
cnt -= 1

for i in visit:
    if i.count(0):
        cnt = -1

print(cnt)