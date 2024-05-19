# 第 398 场周赛 第 4 题
# 题目：100298. 到达第 K 级台阶的方案数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-398/problems/find-number-of-ways-to-reach-the-k-th-stair/
# 题库：https://leetcode.cn/problems/find-number-of-ways-to-reach-the-k-th-stair

from collections import *

d = [defaultdict(int)]
d[0][1] = 1
d[0][0] = 1
for j in range(30):
    t = defaultdict(int)
    p = pow(2, j)
    d_copy = d[-1].copy()
    for k, v in d_copy.items():
        t[k + p] += v  # + d[-1][k + 1] * 2
        if k + p - 1 >= 0:
            t[k + p - 1] += v
    d.append(t)


class Solution:
    def waysToReachStair(self, k: int) -> int:
        ans = 0
        for jump in d:
            ans += jump[k]
        return ans


s = Solution()
examples = [
    (dict(k=0), 2),
    (dict(k=1), 4),
    (dict(k=12345678), 4),
]
for e, a in examples:
    print(a, e)
    print(s.waysToReachStair(**e))
