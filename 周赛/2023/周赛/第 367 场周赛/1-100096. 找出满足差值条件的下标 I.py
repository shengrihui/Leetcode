from typing import List


# 题目：100096. 找出满足差值条件的下标 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-367/problems/find-indices-with-index-and-value-difference-i/
# 题库：https://leetcode.cn/problems/find-indices-with-index-and-value-difference-i/
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]


s = Solution()
examples = [
    (dict(nums=[5, 1, 4, 1], indexDifference=2, valueDifference=4), [0, 3]),
    (dict(nums=[2, 1], indexDifference=0, valueDifference=0), [0, 0]),
    (dict(nums=[1, 2, 3], indexDifference=2, valueDifference=4), [-1, -1]),
]
for e, a in examples:
    print(a, e)
    print(s.findIndices(**e))
