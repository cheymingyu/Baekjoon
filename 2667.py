# 단지번호 붙이기

N = int(input())

matrix = [list(map(int, list(input()))) for _ in range(N)]
for i in matrix:
    print(i)
    
visit = [[0]*N for _ in range(N)]
house = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]
house_num = 0

def dfs(x,y,n):
    global house_num
    visit[x][y] = 1
    matrix[x][y] = n
    house_num += 1

    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if matrix[nx][ny] == 1 and visit[nx][ny] == 0:
                dfs(nx,ny,n)

cnt = 1
for x in range(N):
    for y in range(N):
        if matrix[x][y] == 1 and visit[x][y] == 0:
            dfs(x,y,cnt)
            house.append(house_num)
            house_num = 0

print(len(house))
for i in sorted(house):
    print(i)