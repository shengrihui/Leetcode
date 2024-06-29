# 第 387 场周赛 第 1 题
# 题目：100243. 将元素分配到两个数组中 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-387/problems/distribute-elements-into-two-arrays-i/
# 题库：https://leetcode.cn/problems/distribute-elements-into-two-arrays-i

from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]
        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1 + arr2


s = Solution()
examples = [
    (dict(nums=[2, 1, 3]), [2, 3, 1]),
    (dict(nums=[5, 4, 3, 8]), [5, 3, 4, 8]),
]
for e, a in examples:
    print(a, e)
    print(s.resultArray(**e))
