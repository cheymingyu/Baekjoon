# 미로 탐색

N,M = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(N)]

for i in matrix:
    print(i)
print()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visit = [[0]*M for _ in range(N)]
distance = [[0]*M for _ in range(N)]

for i in visit:
    print(i)
print()

for i in distance:
    print(i)
print()

queue = []
queue.append((0,0))
visit[0][0] = 1
distance[0][0] = 1

while queue:
    x, y = queue.pop(0)
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= ny < M and 0 <= nx < N:
            if visit[nx][ny] == 0 and matrix[nx][ny] == 1:
                queue.append((nx,ny))
                visit[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1

for i in visit:
    print(i)
print()

for i in distance:
    print(i)
print()

print(distance[N-1][M-1])