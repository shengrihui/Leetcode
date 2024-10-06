# 第 418 场周赛 第 4 题
# 题目：100436. 查询排序后的最大公约数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-418/problems/sorted-gcd-pair-queries/
# 题库：https://leetcode.cn/problems/sorted-gcd-pair-queries

from typing import List


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        pass


s = Solution()
examples = [
    (dict(nums=[2, 3, 4], queries=[0, 2, 2]), [1, 2, 2]),
    (dict(nums=[4, 4, 2, 1], queries=[5, 3, 1, 0]), [4, 2, 1, 1]),
    (dict(nums=[2, 2], queries=[0, 0]), [2, 2]),
]
for e, a in examples:
    print(a, e)
    print(s.gcdValues(**e))
