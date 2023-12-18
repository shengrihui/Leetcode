from collections import *
from typing import List


# 题目：100149. 找出缺失和重复的数字
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-376/problems/find-missing-and-repeated-values/
# 题库：https://leetcode.cn/problems/find-missing-and-repeated-values

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        cnt = defaultdict(int)
        n = len(grid)
        for i in range(n):
            for j in range(n):
                cnt[grid[i][j]] += 1
        ans = [0, 0]
        for i in range(1, n * n + 1):
            if cnt[i] == 0:
                ans[1] = i
            elif cnt[i] == 2:
                ans[0] = i
        return ans


s = Solution()
examples = [
    (dict(grid=[[1, 3], [2, 2]]), [2, 4]),
    (dict(grid=[[9, 1, 7], [8, 9, 2], [3, 4, 6]]), [9, 5]),
]
for e, a in examples:
    print(a, e)
    print(s.findMissingAndRepeatedValues(**e))
