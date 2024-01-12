from typing import List


# 题目：100150. 移除后集合的最多元素数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-379/problems/maximum-size-of-a-set-after-removals/
# 题库：https://leetcode.cn/problems/maximum-size-of-a-set-after-removals

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1) // 2, len(nums2) // 2
        a, b = set(nums1), set(nums2)
        ab, only_a, only_b = a & b, a - b, b - a
        abn, only_a_n, only_b_n = len(ab), len(only_a), len(only_b)
        ans = 0
        ans += only_a_n if only_a_n <= n1 else n1
        d = n1 - only_a_n if only_a_n <= n1 else 0
        t = min(abn, d)  # 从 ab 中分出 t 个给 a
        ans += t
        abn -= t

        ans += only_b_n if only_b_n <= n2 else n2
        d = n2 - only_b_n if only_b_n <= n2 else 0
        t = min(abn, d)
        ans += t
        abn -= t
        return ans


s = Solution()
examples = [
    (dict(nums1=[1, 2, 1, 2], nums2=[1, 1, 1, 1]), 2),
    (dict(nums1=[1, 2, 3, 4, 5, 6], nums2=[2, 3, 2, 3, 2, 3]), 5),
    (dict(nums1=[1, 1, 2, 2, 3, 3], nums2=[4, 4, 5, 5, 6, 6]), 6),
]
for e, a in examples:
    print(a, e)
    print(s.maximumSetSize(**e))
