# 阶段变量: k表示已经尝试偷窃了k个房间 0 <= k <= K-1
# 状态变量: xk表示k阶段可以选择的房间
# 决策: uk=1，0表示k阶段是否能选择第k个房间
# 最优指标函数: fx(xk)表示前k个房间偷窃最高金额
# 状态转移方程: xk-1 = xk - uk - 1
# 规划方程: fk(xk)=max|uk=0,1 max{fk-1(xk-uk-1)+uk*V[k]}
# 边界: f0(0) = V[0] f1(xk)=max{V[0], V[1]}
f = lambda: map(int, input().split())

V = list(f())
K = len(V)
dp = [0 for i in range(K)]
# print(dp)
if K == 0:
    print(0)
    exit(0)
dp[0] = V[0]
if 1 < K:
    dp[1] = max(V[0], V[1])

for k in range(2, K):
    dp[k] = max(dp[k - 1], dp[k - 2] + V[k])

print(dp[K - 1])
