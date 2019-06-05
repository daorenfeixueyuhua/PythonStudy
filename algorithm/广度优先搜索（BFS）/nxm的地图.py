# f = lambda:map(int, input().split())
# n, m = f()
#
# g = [''] * n
#
# for i in range(n):
#     g[i] = input()

n = 9
m = 11
v = [[0] * m for i in range(n)]
g = ['.#.........',
     '.#.#######.',
     '.#.#.....#.',
     '.#.#.###.#.',
     '.#.#..@#.#.',
     '.#.#####.#.',
     '.#.......#.',
     '.#########.',
     '...........']

# 找到起点
si, sj = 0, 0
for i in range(n):
    for j in range(m):
        if g[i][j] == '@':
            si = i
            sj = j
print('节点坐标：')
print(si, sj)

# 节点访问顺序
l = []


def bfs(i, j):
    c = 0
    # Q为重点
    Q = [(i, j)]
    while Q:
        c += 1
        i, j = Q[0]
        l.append((i, j))
        # print(g[i][j])
        # 对上下左右的点进行判断，将为访问、不再等待访问队列Q中、且值为 '.' 的节点，加入Q中
        if 0 < j and not v[i][j-1] and (i, j-1) not in Q and g[i][j-1] == '.':
            Q.append((i, j-1))
        if j < m-1 and not v[i][j+1] and (i, j+1) not in Q and g[i][j+1] == '.':
            Q.append((i, j+1))
        if 0 < i and not v[i-1][j] and (i-1, j) not in Q and g[i-1][j] == '.':
            Q.append((i-1, j))
        if i < n-1 and not v[i+1][j] and (i+1, j) not in Q and g[i+1][j] == '.':
            Q.append((i+1, j))
        # mark (i, j)
        v[i][j] = 1
        # 将访问结束的节点从Q中去除
        Q.remove((i, j))
    return c


# 从起点开始dfs
print(bfs(si, sj))
print('节点访问顺序：')
print(l)