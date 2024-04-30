# 第 395 场周赛 第 1 题
# 题目：100285. 找出与数组相加的整数 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-395/problems/find-the-integer-added-to-array-i/
# 题库：https://leetcode.cn/problems/find-the-integer-added-to-array-i

from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1.sort()
        # nums2.sort()
        # return nums2[0] - nums1[0]
        return min(nums2) - min(nums1)


s = Solution()
examples = [
    (dict(nums1=[2, 6, 4], nums2=[9, 7, 5]), 3),
    (dict(nums1=[10], nums2=[5]), -5),
    (dict(nums1=[1, 1, 1, 1], nums2=[1, 1, 1, 1]), 0),
]
for e, a in examples:
    print(a, e)
    print(s.addedInteger(**e))
