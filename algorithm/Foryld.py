def forlyd(g):
    for k in range(len(g)):
        for i in range(len(g)):
            for j in range(len(g)):
                g[i][j] = min(g[i][j], g[i][k]+g[k][j])
    return g


f = lambda: map(int, input().split())

n, m = f()
g = [[999]*n for i in range(n)]
for k in range(m):
    i, j, d = f()
    g[i][j] = d
# g = [[0, 1, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 0, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0]]


print(g)
print(forlyd(g))

