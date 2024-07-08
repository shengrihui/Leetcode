# 题目：100139. 循环移位后的矩阵相似检查
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-373/problems/matrix-similarity-after-cyclic-shifts/
# 题库：https://leetcode.cn/problems/matrix-similarity-after-cyclic-shifts
from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        for i in range(n):
            for j in range(n):
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
        return True


s = Solution()
examples = [
    (dict(mat=[[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], k=2), True),
    (dict(mat=[[2, 2], [2, 2]], k=3), True),
    (dict(mat=[[1, 2]], k=1), False),
]
for e, a in examples:
    print(a, e)
    print(s.areSimilar(**e))
