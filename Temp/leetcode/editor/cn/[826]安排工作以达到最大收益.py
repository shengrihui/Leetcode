# 826 安排工作以达到最大收益
# https://leetcode.cn/problems/most-profit-assigning-work/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        ans = j = mx = 0
        for w in worker:
            while j < len(jobs) and jobs[j][0] <= w:
                mx = max(mx, jobs[j][1])
                j += 1
            ans += mx
        return ans


"""
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        a = sorted(zip(difficulty, profit))
        b = [0] * (max(difficulty + worker) + 1)
        m = 0
        for diff, p in a:
            if p > m:
                m = p
            b[diff] = m
        for i in range(1, len(b)):
            if b[i] == 0:
                b[i] = b[i - 1]
        return sum(b[w] for w in worker)
"""
# leetcode submit region end(Prohibit modification and deletion)
