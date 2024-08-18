# 第 137 场双周赛 第 3 题
# 题目：100407. 放三个车的价值之和最大 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-137/problems/maximum-value-sum-by-placing-three-rooks-i/
# 题库：https://leetcode.cn/problems/maximum-value-sum-by-placing-three-rooks-i

from math import inf
from typing import List


class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        a = []
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                a.append((x, i, j))
        a.sort(reverse=True)
        ans = -inf
        n = len(a)
        for i in range(n):
            s, x, y = a[i]
            if s * 3 <= ans:
                return ans
            for j in range(i + 1, n):
                b, xx, yy = a[j]
                if s + b * 2 <= ans:
                    break
                if xx == x or yy == y:
                    continue
                ns = s + b
                for k in range(j + 1, n):
                    c, xxx, yyy = a[k]
                    if xxx == xx or xxx == x or yyy == yy or yyy == y:
                        continue
                    ns += c
                    ans = max(ans, ns)
                    break
        return ans


s = Solution()
examples = [
    (dict(board=[[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]]), 4),
    (dict(board=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 15),
    (dict(board=[[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.maximumValueSum(**e))
