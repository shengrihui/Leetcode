from typing import List


# 题目：100101. 找出满足差值条件的下标 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-367/problems/find-indices-with-index-and-value-difference-ii/
# 题库：https://leetcode.cn/problems/find-indices-with-index-and-value-difference-ii/submissions/
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        max_index = min_index = 0
        for j in range(indexDifference, len(nums)):
            # 因为是 abs(j-i)>=indexDifference，所以遍历j，维护i左边数组的信息
            i = j - indexDifference
            if nums[i] > nums[max_index]:
                max_index = i
            # 为什么可以用 elif
            # 因为 nums[i] 如果比之前记录的最大值还大了，那一定不会比最小值小
            elif nums[i] < nums[min_index]:
                min_index = i

            # 为什么可以去掉绝对值的计算
            # 如果 nums[j] - nums[max_index] >= valueDifference
            # 那么 第二个 if 也一定成立
            if nums[max_index] - nums[j] >= valueDifference:
                return [max_index, j]
            if nums[j] - nums[min_index] >= valueDifference:
                return [min_index, j]
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
