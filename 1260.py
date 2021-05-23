# DFS와 BFS

N,M,V = map(int, input().split())
matrix = [[0]*(N+1) for i in range(N+1)]
for i in matrix:
    print(i)

for i in range(M):
    a,b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
for i in matrix:
    print(i)

visit_list = [0]*(N+1)
print(visit_list)

def dfs(V):
    visit_list[V] = 1
    print(V, end=' ')
    for i in range(1, N+1):
        if (matrix[V][i] == 1 and visit_list[i] == 0):
            dfs(i)

def bfs(V):
    queue = [V]
    visit_list[V] = 0
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(matrix[V][i] == 1 and visit_list[i] == 1):
                queue.append(i)
                visit_list[i] = 0


dfs(V)
print()
bfs(V)