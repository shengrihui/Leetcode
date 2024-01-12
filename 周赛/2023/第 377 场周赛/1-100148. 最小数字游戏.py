from typing import List


# 题目：100148. 最小数字游戏
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-377/problems/minimum-number-game/
# 题库：https://leetcode.cn/problems/minimum-number-game

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums


s = Solution()
examples = [
    (dict(nums=[5, 4, 2, 3]), [3, 2, 5, 4]),
    (dict(nums=[2, 5]), [5, 2]),
]
for e, a in examples:
    print(a, e)
    print(s.numberGame(**e))
