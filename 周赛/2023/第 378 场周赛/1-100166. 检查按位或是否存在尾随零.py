from typing import List


# 题目：100166. 检查按位或是否存在尾随零
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-378/problems/check-if-bitwise-or-has-trailing-zeros/
# 题库：https://leetcode.cn/problems/check-if-bitwise-or-has-trailing-zeros

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] | nums[j]) & 1 == 0:
                    return True
        return False


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4, 5]), true),
    (dict(nums=[2, 4, 8, 16]), true),
    (dict(nums=[1, 3, 5, 7, 9]), false),
]
for e, a in examples:
    print(a, e)
    print(s.hasTrailingZeros(**e))
