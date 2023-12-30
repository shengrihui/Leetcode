# 2059 转化数字的最小运算数
# https://leetcode.cn/problems/minimum-operations-to-convert-number/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# 双向BFS
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q1, q2 = deque([start]), deque([goal])
        s1, s2 = {start}, {goal}
        ans = 0
        while q1 and q2:
            q, s, vis = (q1, s2, s1) if len(q1) <= len(q2) else (q2, s1, s2)
            for _ in range(len(q)):
                x = q.popleft()
                for i in nums:
                    nxt = [x + i, x - i, x ^ i]
                    for j in nxt:
                        if j in s:
                            return ans + 1
                        if j not in vis and 0 <= j <= 1000:
                            q.append(j)
                            vis.add(j)
            ans += 1
        return -1


# 常规BFS
"""
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = deque([start])
        ans = 0
        vis = set([start])
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                if x < 0 or x > 1000:
                    continue
                for i in nums:
                    nxt = [x + i, x - i, x ^ i]
                    for j in nxt:
                        if j == goal:
                            return ans + 1
                        if j not in vis:
                            q.append(j)
                            vis.add(j)
            ans += 1
        return -1
"""
# leetcode submit region end(Prohibit modification and deletion)
