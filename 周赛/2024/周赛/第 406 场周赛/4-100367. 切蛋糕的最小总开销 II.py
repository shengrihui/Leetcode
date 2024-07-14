# 第 406 场周赛 第 4 题
# 题目：100367. 切蛋糕的最小总开销 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-406/problems/minimum-cost-for-cutting-cake-ii/
# 题库：https://leetcode.cn/problems/minimum-cost-for-cutting-cake-ii

from typing import List


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        ans = h = v = 0
        cnt_h, cnt_v = 1, 1  # 有多少个横/竖
        while v < n - 1 or h < m - 1:
            if v == n - 1 or h < m - 1 and horizontalCut[h] > verticalCut[v]:  # 横切  v==n-1 没法竖切了
                ans += horizontalCut[h] * cnt_v
                h += 1
                cnt_h += 1
            else:
                ans += verticalCut[v] * cnt_h
                v += 1
                cnt_v += 1
        return ans


s = Solution()
examples = [
    (dict(m=3, n=2, horizontalCut=[1, 3], verticalCut=[5]), 13),
    (dict(m=2, n=2, horizontalCut=[7], verticalCut=[4]), 15),
]
for e, a in examples:
    print(a, e)
    print(s.minimumCost(**e))
