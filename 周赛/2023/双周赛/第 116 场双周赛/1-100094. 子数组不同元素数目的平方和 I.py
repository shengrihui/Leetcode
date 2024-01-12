from typing import List


# 题目：100094. 子数组不同元素数目的平方和 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-116/problems/subarrays-distinct-element-sum-of-squares-i/

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                s = set(nums[i:j + 1])
                ans += len(s) ** 2
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 2, 1]), 15),
    (dict(nums=[2, 2]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.sumCounts(**e))
