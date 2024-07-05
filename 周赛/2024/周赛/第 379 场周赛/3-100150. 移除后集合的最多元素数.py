# 题目：100150. 移除后集合的最多元素数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-379/problems/maximum-size-of-a-set-after-removals/
# 题库：https://leetcode.cn/problems/maximum-size-of-a-set-after-removals
from typing import List


# 数组大小的一半 m
# nums1 nums2 去重之后为 a b
# 二者的交集 ab，只有是 a 有 b 没有的 only_a，only_b 同
#
# 如果 only_a 的大小不到 m，就把 only_a 全部加到答案里
#       然后再从 ab 中分一部分来，使得 nums 移除元素之后能够 m
#       但如果 ab 全部分给 ab 之后仍然不够 m 也就无所谓了，说明 len(a) 本身就不够 m
# 如果 only_a 的大小超过 m，就把 m 个加到答案里
# 对 only_b 也一样的操作

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1) // 2
        a, b = set(nums1), set(nums2)
        ab, only_a, only_b = a & b, a - b, b - a
        abn, only_a_n, only_b_n = len(ab), len(only_a), len(only_b)
        ans = 0

        ans += only_a_n if only_a_n <= m else m
        d = m - only_a_n if only_a_n <= m else 0
        t = min(abn, d)  # 从 ab 中分出 t 个给 a
        ans += t
        abn -= t

        ans += only_b_n if only_b_n <= m else m
        d = m - only_b_n if only_b_n <= m else 0
        t = min(abn, d)
        ans += t

        return ans


# 灵神 https://leetcode.cn/problems/maximum-size-of-a-set-after-removals/solutions/2594380/tan-xin-pythonjavacgo-by-endlesscheng-ymuh

s = Solution()
examples = [
    (dict(nums1=[1, 1, 1, 1], nums2=[12, 23, 41, 9]), 3),
    (dict(nums1=[1, 2, 1, 2], nums2=[1, 1, 1, 1]), 2),
    (dict(nums1=[1, 2, 3, 4, 5, 6], nums2=[2, 3, 2, 3, 2, 3]), 5),
    (dict(nums1=[1, 1, 2, 2, 3, 3], nums2=[4, 4, 5, 5, 6, 6]), 6),
]
for e, a in examples:
    print(a, e)
    print(s.maximumSetSize(**e))
