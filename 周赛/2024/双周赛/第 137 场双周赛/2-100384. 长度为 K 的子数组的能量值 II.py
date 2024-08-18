# 第 137 场双周赛 第 2 题
# 题目：100384. 长度为 K 的子数组的能量值 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-137/problems/find-the-power-of-k-size-subarrays-ii/
# 题库：https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-ii

from itertools import *
from typing import List


# 相邻两个后一个比前一个大 1 记 0，否则记 1
# 然后以此计算前缀和
# 然后就是看长度为 k 的子数组的和是不是 0 来添加答案
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        a = [0 if y - x == 1 else 1 for x, y in pairwise(nums)]
        s = list(accumulate(a, initial=0))
        n = len(nums)
        ans = []
        for i in range(k, n + 1):
            if s[i - 1] - s[i - k] == 0:
                ans.append(nums[i - 1])
            else:
                ans.append(-1)
        return ans


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * (n - k + 1)
        cnt = 0  # 连续递增的长度
        for i, x in enumerate(nums):
            if i == 0 or x - nums[i - 1] == 1:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:  # x 记到 i - k + 1 位置上
                ans[i - k + 1] = x
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4, 3, 2, 5], k=3), [3, 4, -1, -1, -1]),
    (dict(nums=[2, 2, 2, 2, 2], k=4), [-1, -1]),
    (dict(nums=[3, 2, 3, 2, 3, 2], k=2), [-1, 3, -1, 3, -1]),
]
for e, a in examples:
    print(a, e)
    print(s.resultsArray(**e))
