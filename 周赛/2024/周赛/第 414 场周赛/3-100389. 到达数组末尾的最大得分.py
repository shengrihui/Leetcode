# 第 414 场周赛 第 3 题
# 题目：100389. 到达数组末尾的最大得分
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-414/problems/reach-end-of-array-with-max-score/
# 题库：https://leetcode.cn/problems/reach-end-of-array-with-max-score

from typing import List


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        ans = 0
        mx = nums[0]
        for x in nums[:-1]:
            if x > mx:
                mx = x
            ans += mx
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 3, 1, 5]), 7),
    (dict(nums=[4, 3, 1, 3, 2]), 16),
]
for e, a in examples:
    print(a, e)
    print(s.findMaximumScore(**e))
