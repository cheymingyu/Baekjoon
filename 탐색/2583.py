# 영역 구하기

# 입력
M, N, K = map(int, input().split())
coordinate = []
for i in range(K):
    coordinate.append(list(map(int, input().split())))

# 모눈종이 초기화
paper = [[0]*N for i in range(M)]
visit = [[0]*N for i in range(M)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 모눈종이 1로 채우기
for c in coordinate:
    x1 = c[0]
    y1 = c[1]
    x2 = c[2]
    y2 = c[3]
    
    for y in range(y1, y2):
        for x in range(x1, x2):
            paper[y][x] = 1
            

cnt = 0
area = []
# 모든 좌표 돌며 넓이 계산
for i in range(M):
    for j in range(N):
        # paper[i][j]가 0이면 그 주위 0인 블록 모두 계산해서 넓이 구하기
        if paper[i][j] == 0:
            cnt = 1
            queue = [(i, j)]
            paper[i][j] = 1
            while queue:
                x, y = queue.pop(0)
                for k in range(4):
                    x1 = x + dx[k]
                    y1 = y + dy[k]
                    if 0 <= x1 < M and 0 <= y1 < N and paper[x1][y1] == 0:
                        paper[x1][y1] = 1
                        queue.append((x1, y1))
                        cnt += 1
            area.append(cnt)
            
print(len(area))
area.sort()
for a in area:
    print(a, end=' ')