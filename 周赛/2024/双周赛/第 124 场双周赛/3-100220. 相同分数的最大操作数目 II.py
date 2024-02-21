# 第 124 场双周赛 第 3 题
# 题目：100220. 相同分数的最大操作数目 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-124/problems/maximum-number-of-operations-with-the-same-score-ii/
# 题库：https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-ii

from functools import *
from typing import List

# BFS 超内存
"""
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        q = deque()
        n = len(nums)
        q.append((2, n - 1, nums[0] + nums[1]))
        q.append((1, n - 2, nums[0] + nums[-1]))
        q.append((0, n - 3, nums[-1] + nums[-2]))
        ans = 0
        while q:
            for _ in range(len(q)):
                i, j, s = q.popleft()
                if i >= n or j <= i or j < 0:
                    continue
                if nums[i + 1] + nums[i] == s:
                    q.append((i + 2, j, s))
                if nums[i] + nums[j] == s:
                    q.append((i + 1, j - 1, s))
                if nums[j] + nums[j - 1] == s:
                    q.append((i, j - 2, s))
            ans += 1
        return ans
"""


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @cache
        def dfs(i: int, j: int, s: int) -> int:
            if j <= i:
                return 0
            res = 0
            if nums[i + 1] + nums[i] == s:
                res = max(res, 1 + dfs(i + 2, j, s))
            if nums[i] + nums[j] == s:
                res = max(res, 1 + dfs(i + 1, j - 1, s))
            if nums[j] + nums[j - 1] == s:
                res = max(res, 1 + dfs(i, j - 2, s))
            return res

        n = len(nums)
        return 1 + max(dfs(2, n - 1, nums[0] + nums[1]),
                       dfs(1, n - 2, nums[0] + nums[-1]),
                       dfs(0, n - 3, nums[-1] + nums[-2]))
        # best = n // 2
        # r1 = dfs(2, n - 1, nums[0] + nums[1]) + 1
        # if r1 == best:
        #     return r1
        # r2 = dfs(1, n - 2, nums[0] + nums[-1]) + 1
        # if r2 == best:
        #     return r2
        # r3 = dfs(0, n - 3, nums[-1] + nums[-2]) + 1
        # return max(r1, r2, r3)


# 飞快的方法
"""
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        best = len(nums) // 2
        self.ans = 1
        @cache
        def dfs(target:int, l, r, times:int):
            if self.ans == best:
                return best
            if l + 1 > r:
                self.ans = times
                return
            t1, t2, t3 = sum(nums[l: l+2]), sum(nums[r:r-2:-1]), nums[l] + nums[r]
            if t1 == target:
                dfs(target, l+2, r, times+1)
            if t2 == target:
                dfs(target, l, r-2, times+1)
            if t3 == target:
                dfs(target, l+1, r-1, times+1)
            if times > self.ans:
                self.ans = times
            return
        t1, t2, t3 = sum(nums[:2]), sum(nums[:-3:-1]), nums[0] + nums[-1]
        l = 0
        r = len(nums)-1
        dfs(t1, l+2, r, 1)
        if self.ans == best:
            return best
        dfs(t2, l, r-2, 1)
        if self.ans == best:
            return best
        dfs(t3, l+1, r-1, 1)
        return self.ans
             
            
"""

s = Solution()
examples = [
    (dict(nums=[3, 2, 1, 2, 3, 4]), 3),
    (dict(nums=[3, 2, 6, 1, 4]), 2),
    (dict(nums=[1, 9, 7, 3, 2, 7, 4, 12, 2, 6]), 2),
]
for e, a in examples:
    print(a, e)
    print(s.maxOperations(**e))
