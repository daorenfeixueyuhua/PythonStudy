# f = lambda:map(int, input().split())
# n, m = f()
# g = [[0]*(n+1) for i in [0]*(n+1)]
# for k in range(m):
#     i, j = f()
#     g[i][j] = 1
# 手动输入数据
g = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for i in range(1, len(g)):
    print(g[i])
# 记录拓扑排序顺序
l = []
# 记录出度为0的点
s = []
# 记录已经访问的点
v = []
for i in range(1, len(g)):
    if g[i].__eq__([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
        s.append(i)


# 好像大概是完成了的，但是应该是有问题的
def visit(g, n):
    if n not in v:
        v.append(n)
    for m in range(1, len(g)):
        if g[m][n] and m not in v:
            visit(g, m)
    # 核心之处，代理解
    l.append(n)


# 对s中的点进行dfs访问
for n in s:
    visit(g, n)

print('拓扑排序：')
print(l)
print('访问节点顺序：')
print(v)
print('出度为0节点集合：')
print(s)
