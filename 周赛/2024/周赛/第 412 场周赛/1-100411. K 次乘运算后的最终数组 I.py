# 第 412 场周赛 第 1 题
# 题目：100411. K 次乘运算后的最终数组 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-412/problems/final-array-state-after-k-multiplication-operations-i/
# 题库：https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-i

from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            mn, mni = nums[0], 0
            for i in range(1, len(nums)):
                if nums[i] < mn:
                    mn, mni = nums[i], i
            nums[mni] *= multiplier
        return nums


s = Solution()
examples = [
    (dict(nums=[5, 3], k=5, multiplier=5), [125, 375]),
    (dict(nums=[2, 3, 4, 1, 1, 1, 5], k=4, multiplier=2), [4, 3, 4, 2, 2, 2, 5]),
    (dict(nums=[2, 1, 3, 5, 6], k=5, multiplier=2), [8, 4, 6, 5, 6]),
    (dict(nums=[1, 2], k=3, multiplier=4), [16, 8]),
    (dict(nums=[2, 1], k=1, multiplier=2), [2, 2]),
    (dict(nums=[3, 9, 27, 81], k=10, multiplier=3), [243, 243, 243, 243]),
]
for e, a in examples:
    print(a, e)
    print(s.getFinalState(**e))
