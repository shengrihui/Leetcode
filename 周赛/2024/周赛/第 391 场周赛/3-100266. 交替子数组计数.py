# 第 391 场周赛 第 3 题
# 题目：100266. 交替子数组计数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-391/problems/count-alternating-subarrays/
# 题库：https://leetcode.cn/problems/count-alternating-subarrays

from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        i = 0
        while i < n:
            st = i
            i += 1
            while i < n and nums[i] != nums[i - 1]:
                i += 1
            s = i - st
            ans += s * (s + 1) // 2
        return ans


s = Solution()
examples = [
    (dict(nums=[0, 1, 1, 1]), 5),
    (dict(nums=[1, 0, 1, 0]), 10),
]
for e, a in examples:
    print(a, e)
    print(s.countAlternatingSubarrays(**e))
