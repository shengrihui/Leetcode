# 第 124 场双周赛 第 1 题
# 题目：100221. 相同分数的最大操作数目 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-124/problems/maximum-number-of-operations-with-the-same-score-i/
# 题库：https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-i

from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        s = nums[0] + nums[1]
        for i in range(0, 2 * (n // 2), 2):
            x, y = nums[i], nums[i + 1]
            if x + y == s:
                ans += 1
            else:
                break
        return ans


s = Solution()
examples = [
    (dict(nums=[3, 2, 1, 4, 5]), 2),
    (dict(nums=[3, 2, 6, 1, 4]), 1),
]
for e, a in examples:
    print(a, e)
    print(s.maxOperations(**e))
