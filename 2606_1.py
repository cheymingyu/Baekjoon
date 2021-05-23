#바이러스

V = int(input())
E = int(input())

edge = []
for _ in range(E):
    a, b = map(int, input().split())
    edge.append([a,b])

parent = [-1]*(V+1)

def find(member):
    root = member
    while parent[root] >= 0:
        root = parent[root]
    return root

def union(rootA, rootB):
    if parent[rootA] >= parent[rootB]:
        parent[rootB] += parent[rootA]
        parent[rootA] = rootB
    else:
        parent[rootA] += parent[rootB]
        parent[rootB] = rootA

for i in range(E):
    a, b = edge[i]
    a = find(a)
    b = find(b)
    if a != b:
        union(a, b)

print(abs(parent[find(1)])-1)