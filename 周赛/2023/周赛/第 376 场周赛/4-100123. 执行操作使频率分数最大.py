from itertools import *
from typing import List


# 题目：100123. 执行操作使频率分数最大
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-376/problems/apply-operations-to-maximize-frequency-score/
# 题库：https://leetcode.cn/problems/apply-operations-to-maximize-frequency-score

# 中位数贪心 + 滑动窗口
# 先排序
# 然后滑窗，计算窗口内的元素都变成中位数需要的操作次数
# 如何计算窗口内的数都变成中位数的操作次数？
# [2602 使数组元素全部相等的最少操作次数]
# https://leetcode.cn/problems/minimum-operations-to-make-all-array-elements-equal/submissions/489676928/
class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        def distance_sum(l: int, r: int) -> int:
            m = (l + r) // 2  # 中位数的位置，无论奇偶（如果是偶数，中间的两个都可以）
            # 想好 l,m,r 谁要谁不要
            left = (m - l + +1) * nums[m] - (pre_sum[m + 1] - pre_sum[l])
            right = (pre_sum[r + 1] - pre_sum[m + 1]) - (r - m) * nums[m]
            return left + right

        nums.sort()
        n = len(nums)
        pre_sum = list(accumulate(nums, initial=0))  # 前缀和
        left = ans = 0
        for right in range(n):
            while distance_sum(left, right) > k:
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# https://www.bilibili.com/video/BV1994y1A7oo/
# class Solution:
#     def maxFrequencyScore(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         ans = left = s = 0  # s 是窗口元素与窗口中位数的差之和
#         for right, x in enumerate(nums):
#             s += x - nums[(left + right) // 2]
#             while s > k:
#                 s += nums[left] - nums[(left + right + 1) // 2]
#                 left += 1
#             ans = max(ans, right - left + 1)
#         return ans
#
# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/apply-operations-to-maximize-frequency-score/solutions/2569301/hua-dong-chuang-kou-zhong-wei-shu-tan-xi-nuvr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

s = Solution()
examples = [
    (dict(nums=[1, 2, 6, 4], k=3), 3),
    (dict(nums=[1, 4, 4, 2, 4], k=0), 3),
]
for e, a in examples:
    print(a, e)
    print(s.maxFrequencyScore(**e))
