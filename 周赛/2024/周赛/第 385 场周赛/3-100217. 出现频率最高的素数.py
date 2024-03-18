# 第 385 场周赛 第 3 题
# 题目：100217. 出现频率最高的素数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-385/problems/most-frequent-prime/
# 题库：https://leetcode.cn/problems/most-frequent-prime

from collections import *
from math import isqrt
from typing import List


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        def isPrime(x: int) -> bool:
            for i in range(2, isqrt(x) + 1):
                if int(x / i) == x / i:
                    return False
            return True

        nums = Counter()
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                for di, dj in [(1, 0), (1, 1), (0, 1), (-1, 1),
                               (-1, 0), (-1, -1), (0, -1), (1, -1)]:
                    d = 1
                    t = mat[i][j]
                    while True:
                        ni, nj = i + d * di, j + d * dj
                        if not (0 <= ni < n and 0 <= nj < m):
                            break
                        a = mat[ni][nj]
                        t = t * 10 + a
                        d += 1
                        if t > 10:
                            nums[t] += 1
        for num, cnt in sorted(nums.items(), key=lambda x: (-x[1], -x[0])):
            if isPrime(num):
                return num

        return -1


s = Solution()
examples = [
    (dict(mat=[[9, 3, 8], [4, 2, 5], [3, 8, 6]]), 823),
    (dict(mat=[[1, 1], [9, 9], [1, 1]]), 19),
    (dict(mat=[[7]]), -1),
    (dict(mat=[[9, 7, 8], [4, 6, 5], [2, 8, 6]]), 97),
    (dict(mat=[[4, 9], [1, 4]]), 41),
]
for e, a in examples:
    print(a, e)
    print(s.mostFrequentPrime(**e))
