# 바이러스

V = int(input())
E = int(input())

# edge = []
matrix = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1
    # edge.append([a,b])

visit = [0]*(V+1)
c = -1

def dfs(v):
    global c
    visit[v] = 1
    c += 1
    for i in range(1, V+1):
        if(visit[i] == 0 and matrix[v][i] == 1):
            dfs(i)

dfs(1)
print(c)
# print(edge)

# parent = [-1]*(V+1)

# for i in range(E):
#     a, b = edge[i]
#     parent[a] += -1
#     parent[b] = a