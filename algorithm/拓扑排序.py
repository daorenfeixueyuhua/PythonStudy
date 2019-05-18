# f = lambda: map(int, input().split())
#
# n, m = f()
# g = [[0]*(n+1) for i in range(n+1)]
# for k in range(m):
#     i, j = f()
#     g[i][j] = 1


class Edge(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        # 发现该节点的时间
        self.ft = 0
        # 搜索该节点的时间
        self.vt = 0

    def __str__(self):
        return 'id: '+str(self.id) + ' name: ' + self.name + ' ft: ' + str(self.ft) + ' vt:' + str(self.vt)



def dfs(g, s, v, t):
    if s in v:
        return
    # 节点s访问完成
    v.append(s)
    for i in range(1, len(g)):
        if i not in v and g[s][i]:
            # 节点ｉ被发现
            dfs(g, i, v, t)


# 拓扑排序
def topological_sort(g, e):
    # 先进行一次深搜
    v = []
    t = 0
    # 深搜没有问题但是，不和题意

    for i in range(1, len(g)):
        if i not in v:
            dfs(g, i, v, t)
    print(v)
    print(t)



g = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

n = [' ', '内裤', '袜子', '裤子', '鞋', '手表', '腰带', '衬衣', '领带', '夹克']

e = [Edge(i, n[i]) for i in range(0, len(g))]
for i in range(1, len(g)):
    print(e[i])

topological_sort(g, e)

