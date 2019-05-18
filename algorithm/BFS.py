def bfs(g, s):
    V = []  # 已经搜索
    Q = [s] # 待搜索
    while Q:
        s = Q[0]
        # 将　s 的后继放入 Q　中
        for i in range(0, len(g)):
            if i not in V and i not in Q and g[s][i]:
                Q.append(i)
        V.append(s)
        # print(s)
        Q.remove(s)
    return V

# 缺点：只能搜索强连通性的图
def dfs(g, s, V):
    if s in V:
        return V
    V.append(s)
    for i in range(0, len(g)):
        if i not in V and g[s][i]:
            V = dfs(g, i, V)
    return V


f = lambda:map(int, input().split())

# n, m = f()
# n = 8
# m = 9
# 二维ｌｉｓｔ的初始化方法
# g = [[0]*n for _ in range(n)]

g = [[0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]]

# for v in range(0, m):
#     i, j = f()
#     g[i][j] = 1
#     g[j][i] = 1

# print(g)
print(bfs(g, 1))
print(dfs(g, 1, []))