f = lambda: map(int, input().split())
F, M = f()
A = [[0, 0, 0, 0, 0, 0, 0],
     [0, 7, 23, -5, -24, 16],
     [0, 5, 21, -4, 10, 23],
     [0, -21, 5, -4, -20, 20]]

dp = [[0] * (F + 1) for i in range(M + 1)]

for i in range(1, M + 1):
    for j in range(1, F + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + A[j][i])

print(dp)
