# 第 400 场周赛 第 4 题
# 题目：100315. 找到按位与最接近 K 的子数组
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-400/problems/find-subarray-with-bitwise-and-closest-to-k/
# 题库：https://leetcode.cn/problems/find-subarray-with-bitwise-and-closest-to-k
# 新题库： https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/description/

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        N = max(nums).bit_length()
        bits = [[0] * N for _ in range(2)]
        left = 0
        ans = 10 ** 9

        def update(x, add):
            ret = 0
            for j in range(N):
                bits[x >> j & 1][j] += add
                if bits[0][j] == 0 and bits[1][j] > 0:
                    ret |= 1 << j
            return ret

        for right, x in enumerate(nums):
            s = update(x, 1)
            ans = min(ans, abs(k - s))
            while left < right and k >= s:
                s = update(nums[left], -1)
                ans = min(ans, abs(k - s))
                left += 1
        return ans


# 灵神
"""
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf
        for i, x in enumerate(nums):
            ans = min(ans, abs(x - k))
            j = i - 1
            while j >= 0 and nums[j] & x != nums[j]:
                nums[j] &= x
                ans = min(ans, abs(nums[j] - k))
                j -= 1
        return ans
"""

s = Solution()
examples = [
    (dict(nums=[1, 2, 4, 5], k=3), 1),
    (dict(nums=[1, 2, 1, 2], k=2), 0),
    (dict(nums=[1], k=10), 9),
    (dict(nums=[3, 5], k=10), 5),
    (dict(nums=[40, 3, 70, 86, 89], k=57), 7),
    (dict(nums=[7, 8, 9], k=10), 1),
]
for e, a in examples:
    print(a, e)
    print(s.minimumDifference(**e))
