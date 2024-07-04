# 题目：100178. 将数组分成最小总代价的子数组 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-122/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/
# 题库：https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-ii
from typing import List

from sortedcontainers import SortedList


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        k -= 1
        S = SortedList(nums[1:dist + 2])
        ans = sumk = sum(S[:k])  # sumk 前 k 个数的和
        left = 1
        for right in range(dist + 2, n):
            out, in_ = nums[left], nums[right]
            kth = S[k - 1]
            S.add(in_)
            S.remove(out)
            if out <= kth and in_ <= kth:
                sumk = sumk + in_ - out
            elif in_ <= kth < out:
                sumk = sumk + in_ - kth
            elif out <= kth < in_:
                sumk = sumk - out + S[k - 1]
            left += 1
            if sumk < ans:
                ans = sumk
        return ans + nums[0]


s = Solution()
examples = [
    (dict(
        nums=[36, 28, 42, 36, 39, 13, 24, 3, 32, 16, 11, 43, 21, 40, 34, 49, 29, 20, 34, 34, 8, 3, 41, 6, 46, 5, 35, 5,
              47, 2], k=25, dist=26), 570),
    (dict(nums=[25, 13, 22, 14, 42, 14, 34, 12, 25, 15], k=3, dist=1), 60),
    (dict(nums=[2, 5, 3, 5, 7, 4, 3], k=3, dist=3), 9),
    (dict(nums=[1, 5, 3, 7], k=3, dist=1), 9),
    (dict(nums=[2, 6, 3, 8, 3, 1, 1], k=3, dist=4), 4),
    (dict(nums=[1, 6, 5, 8, 11, 10, 6], k=5, dist=3), 31),
    (dict(nums=[1, 1, 1], k=3, dist=1), 3),
    (dict(nums=[1, 3, 2, 6, 4, 2], k=3, dist=3), 5),
    (dict(nums=[10, 1, 2, 2, 2, 1], k=4, dist=3), 15),
    (dict(nums=[10, 8, 18, 9], k=3, dist=1), 36),
]
for e, a in examples:
    print(a, e)
    print(s.minimumCost(**e))
