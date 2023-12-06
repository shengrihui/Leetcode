# 题目：# 4
# 题目链接：https://www.lanqiao.cn/problems/6280/learning/?contest_id=146

from math import gcd, inf

n, m, q = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(map(int, input().split())))

# dp[i][j][q] 在(i,j)还剩 q 个钥匙的情况的最大路径和
dp = [[[-inf for _ in range(q + 1)] for j in range(m)] for i in range(n)]
dp[0][0][-1] = g[0][0]


def f(i, j, ii, jj):
    # i、j 当前，ii、jj上一个
    global dp
    t = g[i][j]
    if gcd(g[i][j], g[ii][jj]) == 1:
        for k in range(q, 0, -1):
            dp[i][j][k - 1] = dp[i][j][k - 1] if dp[i][j][k - 1] > dp[ii][jj][k] + t else dp[ii][jj][k] + t
    else:
        for k in range(q + 1):
            dp[i][j][k] = dp[i][j][k] if dp[i][j][k] > dp[ii][jj][k] + t else dp[ii][jj][k] + t


for i in range(n):
    for j in range(m):
        if i - 1 >= 0:
            f(i, j, i - 1, j)
        if j - 1 >= 0:
            f(i, j, i, j - 1)
ans = max(dp[-1][-1])
print(ans if ans > 0 else -1)

for d in dp:
    print(d)
"""
3 3 1
2 6 7
1 3 9
5 6 8

28
"""
