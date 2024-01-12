from typing import List


# 题目：100161. 划分数组并满足最大差限制
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-376/problems/divide-array-into-arrays-with-max-difference/
# 题库：https://leetcode.cn/problems/divide-array-into-arrays-with-max-difference

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append(nums[i: i + 3])
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2), [[1, 1, 3], [3, 4, 5], [7, 8, 9]]),
    (dict(nums=[1, 3, 3, 2, 7, 3], k=3), []),
]
for e, a in examples:
    print(a, e)
    print(s.divideArray(**e))
