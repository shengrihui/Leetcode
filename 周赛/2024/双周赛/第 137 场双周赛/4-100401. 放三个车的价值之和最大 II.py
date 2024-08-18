# 第 137 场双周赛 第 4 题
# 题目：100401. 放三个车的价值之和最大 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-137/problems/maximum-value-sum-by-placing-three-rooks-ii/
# 题库：https://leetcode.cn/problems/maximum-value-sum-by-placing-three-rooks-ii

from typing import List


# 方法一：同第三题

# 方法二：灵神前后缀分解
# https://leetcode.cn/problems/maximum-value-sum-by-placing-three-rooks-ii/solutions/2884186/qian-hou-zhui-fen-jie-pythonjavacgo-by-e-gc48
class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        pass


s = Solution()
examples = [
    (dict(board=[[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]]), 4),
    (dict(board=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 15),
    (dict(board=[[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.maximumValueSum(**e))
