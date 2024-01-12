from typing import List


# 题目：100120. 找出强数对的最大异或值 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-371/problems/maximum-strong-pair-xor-i/
# 题库：https://leetcode.cn/problems/maximum-strong-pair-xor-i

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            x = nums[i]
            for j in range(i + 1, n):
                y = nums[j]
                if y > 2 * x:
                    break
                xor = x ^ y
                ans = xor if xor > ans else ans
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4, 5]), 7),
    (dict(nums=[10, 100]), 0),
    (dict(nums=[5, 6, 25, 30]), 7),
]
for e, a in examples:
    print(a, e)
    print(s.maximumStrongPairXor(**e))
