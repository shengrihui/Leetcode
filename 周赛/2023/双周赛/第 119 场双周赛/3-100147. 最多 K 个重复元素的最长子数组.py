from collections import *
from typing import List

# 题目：100147. 最多 K 个重复元素的最长子数组
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-119/problems/length-of-longest-subarray-with-at-most-k-frequency/
# 题库：https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency

# 这个方法有点绕，虽然能 ac
"""
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        indies = defaultdict(list)
        # 记录 x 的出现的位置
        for i, x in enumerate(nums):
            indies[x].append(i)
        ans = 0
        left = 0
        for right, x in enumerate(nums):
            cnt[x] += 1  # nums[right] 到 right 的时候，x 的数量多了一个
            if cnt[x] > k:
                # print(indies[x],bisect.bisect_left(indies[x], right))
                next_left_idx = bisect.bisect_left(indies[x], right) - k
                next_left = indies[x][next_left_idx] + 1 # left 指针移动都 next_left 使得范围内 x 的数量再次为 k
                # print(right,next_left)
                while left < next_left:
                    cnt[nums[left]] -= 1
                    left += 1
            ans = max(ans, right - left + 1)
        return ans
"""


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        left = 0
        for right, x in enumerate(nums):
            cnt[x] += 1
            # 这个还是麻烦了
            """
            if cnt[x] > k:  # x 的数量比 k 多了
                # 移动 left 直到“挤下去一个 x
                while nums[left] != x:
                    cnt[nums[left]] -= 1
                    left += 1
                cnt[nums[left]] -= 1
                left += 1
            """
            while cnt[x] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2), 6),
    (dict(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1), 2),
    (dict(nums=[5, 5, 5, 5, 5, 5, 5], k=4), 4),
    (dict(nums=[1, 2, 1, 5], k=1), 3),
    (dict(nums=[2, 1, 1, 2, 3], k=1), 3),
]
for e, a in examples:
    print(a, e)
    print(s.maxSubarrayLength(**e))
