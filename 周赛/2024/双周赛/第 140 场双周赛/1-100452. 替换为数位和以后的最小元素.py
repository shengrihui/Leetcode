# 第 140 场双周赛 第 1 题
# 题目：100452. 替换为数位和以后的最小元素
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-140/problems/minimum-element-after-replacement-with-digit-sum/
# 题库：https://leetcode.cn/problems/minimum-element-after-replacement-with-digit-sum

from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(map(int, str(x))) for x in nums)


s = Solution()
examples = [
    (dict(nums=[10, 12, 13, 14]), 1),
    (dict(nums=[1, 2, 3, 4]), 1),
    (dict(nums=[999, 19, 199]), 10),
]
for e, a in examples:
    print(a, e)
    print(s.minElement(**e))
