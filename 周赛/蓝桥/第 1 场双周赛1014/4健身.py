# 题目：# 4健身
# 题目链接：
from collections import defaultdict

n, m, q = map(int, input().split())
other_days = list(map(int, input().split()))
# plans = []
mp = defaultdict(int)
dp = [0] * (n + 1)
for _ in range(m):
    k, s = map(int, input().split())
    mp[2 ** k] = max(mp[2 ** k], s)
for i in range(1, n + 1):
    for k, s in mp.items():
        if i - k >= 0:
            dp[i] = max(dp[i], dp[i - k] + mp[k])
ans = dp[other_days[0] - 1] + dp[n - other_days[-1]]
for i in range(1, q):
    day1, day2 = other_days[i - 1], other_days[i]
    ans += dp[day2 - day1 - 1]
print(ans)
print(dp)
"""
10 3 3
1 4 9
0 3
1 7
2 20
"""
