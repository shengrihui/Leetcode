from typing import List


# 题目：100130. 找到两个数组中的公共元素
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-119/problems/find-common-elements-between-two-arrays/
# 题库：https://leetcode.cn/problems/find-common-elements-between-two-arrays

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ans = [0, 0]
        # for i in nums1:
        #     if i in nums2:
        #         ans[0] += 1
        # for i in nums2:
        #     if i in nums1:
        #         ans[1] += 1
        # return ans
        # O(n+m)
        set1 = set(nums1)
        set2 = set(nums2)
        cnt1 = sum(x in set2 for x in nums1)
        cnt2 = sum(x in set1 for x in nums2)
        return [cnt1, cnt2]


s = Solution()
examples = [
    (dict(nums1=[4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6]), [3, 4]),
    (dict(nums1=[3, 4, 2, 3], nums2=[1, 5]), [0, 0]),
]
for e, a in examples:
    print(a, e)
    print(s.findIntersectionValues(**e))
