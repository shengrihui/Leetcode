# 题目：100154. 执行操作后的最大分割数量
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-379/problems/maximize-the-number-of-partitions-after-operations/
# 题库：https://leetcode.cn/problems/maximize-the-number-of-partitions-after-operations

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        pass


s = Solution()
examples = [
    (dict(s="accca", k=2), 3),
    (dict(s="aabaab", k=3), 1),
    (dict(s="xxyz", k=1), 4),
]
for e, a in examples:
    print(a, e)
    print(s.maxPartitionsAfterOperations(**e))
