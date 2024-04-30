# 第 395 场周赛 第 2 题
# 题目：100287. 找出与数组相加的整数 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-395/problems/find-the-integer-added-to-array-ii/
# 题库：https://leetcode.cn/problems/find-the-integer-added-to-array-ii

from typing import List

"""
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        cnt1 = Counter(nums1)
        # for x in range(1000, -1002, -1):
        for x in [nums1[2] - nums2[0], nums1[1] - nums2[0], nums1[0] - nums2[0]]:
            cnt2 = Counter()
            for y in nums2:
                if y + x not in nums1:
                    break
                cnt2[y + x] += 1
                if cnt2[y + x] > cnt1[y + x]:
                    break
            else:
                return -x
"""


# x 只能有三种取值
# nums2[0] - nums1[0/1/2]
# 排序之后，为了求最小，从 2 开始枚举
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for i in range(2, -1, -1):
            diff = nums2[0] - nums1[i]  # x
            # 判断子序列 #392 题
            j = 0
            for y in nums1:
                if y + diff == nums2[j]:
                    j += 1
                    if j == len(nums2):
                        return diff


s = Solution()
examples = [
    (dict(nums1=[4, 20, 16, 12, 8], nums2=[14, 18, 10]), -2),
    (dict(nums1=[3, 5, 5, 3], nums2=[7, 7]), 2),
    (dict(nums1=[4, 5, 7], nums2=[5]), -2),
    (dict(nums1=[1, 1, 1, 9, 9], nums2=[5, 5, 5]), 4),
]
for e, a in examples:
    print(a, e)
    print(s.minimumAddedInteger(**e))
