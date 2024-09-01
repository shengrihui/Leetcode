# 第 413 场周赛 第 4 题
# 题目：100408. 查询子数组最大异或值
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-413/problems/maximum-xor-score-subarray-queries/
# 题库：https://leetcode.cn/problems/maximum-xor-score-subarray-queries

from typing import List

"""
f[i][j] nums[i..j] 的异或和
f[i][j] = f[i][j-1] ^ f[i+1][j]
i 从大到小，j 从 i+1 到 n-1 

mx[i][j] nums[i..j] 所有子数组的异或和的最大值
mx[i][j] = max(f[i][j], mx[i][j-1], mx[i+1][j])

"""


class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        mx = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            f[i][i] = mx[i][i] = nums[i]
            for j in range(i + 1, n):
                f[i][j] = f[i][j - 1] ^ f[i + 1][j]
                mx[i][j] = max(f[i][j], mx[i][j - 1], mx[i + 1][j])
        return [mx[l][r] for l, r in queries]


s = Solution()
examples = [
    (dict(nums=[2, 8, 4, 32, 16, 1], queries=[[0, 2], [1, 4], [0, 5]]), [12, 60, 60]),
    (dict(nums=[0, 7, 3, 2, 8, 5, 1], queries=[[0, 3], [1, 5], [2, 4], [2, 6], [5, 6]]), [7, 14, 11, 14, 5]),
]
for e, a in examples:
    print(a, e)
    print(s.maximumSubarrayXor(**e))
