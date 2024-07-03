# 第 125 场双周赛 第 2 题
# 题目：100232. 超过阈值的最少操作数 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-125/problems/minimum-operations-to-exceed-threshold-value-ii/
# 题库：https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-ii
import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heapq.heapify(nums)
        while nums[0] < k:
            x = heapq.heappop(nums)
            heapq.heapreplace(nums, 2 * x + nums[0])
            ans += 1
        return ans


s = Solution()
examples = [
    (dict(nums=[2, 11, 10, 1, 3], k=10), 2),
    (dict(nums=[1, 1, 2, 4, 9], k=20), 4),
]
for e, a in examples:
    print(a, e)
    print(s.minOperations(**e))
