# 第 123 场双周赛 第 1 题
# 题目：100222. 三角形类型 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-123/problems/type-of-triangle-ii/
# 题库：https://leetcode.cn/problems/type-of-triangle-ii

from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        if a + b <= c or a + c <= b or b + c <= a:
            return "none"
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            return "isosceles"

        return "scalene"


s = Solution()
examples = [
    (dict(nums=[3, 3, 3]), "equilateral"),
    (dict(nums=[3, 4, 5]), "scalene"),
    (dict(nums=[8, 4, 4]), "none"),
]
for e, a in examples:
    print(a, e)
    print(s.triangleType(**e))
