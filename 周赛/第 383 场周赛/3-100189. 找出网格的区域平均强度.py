# 第 383 场周赛 第 3 题
# 题目：100189. 找出网格的区域平均强度
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-383/problems/find-the-grid-of-region-average/
# 题库：https://leetcode.cn/problems/find-the-grid-of-region-average

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *


class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        cnt = [[0] * (m + 1) for _ in range(n + 1)]
        avg = [[0] * (m + 1) for _ in range(n + 1)]
        pre = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                pre[i + 1][j + 1] = pre[i + 1][j] + pre[i][j + 1] - pre[i][j] + image[i][j]
        # print(pre)
        for i in range(n - 2):
            j = 0
            while j < m - 2:
                flag = True
                for x in [i, i + 1, i + 2]:
                    for y in [j, j + 1]:
                        if abs(image[x][y] - image[x][y + 1]) > threshold:
                            flag = False
                            break
                    if not flag: break
                if not flag:
                    j+=1
                    continue
                for x in [i, i + 1]:
                    for y in [j, j + 1, j + 2]:
                        if abs(image[x][y] - image[x + 1][y]) > threshold:
                            flag = False
                            break
                    if not flag: break
                if flag:  # 这是一个区域
                    s = pre[i + 3][j + 3] - pre[i + 3][j] - pre[i][j + 3] + pre[i][j]
                    for x in range(i, i + 3):
                        for y in range(j, j + 3):
                            cnt[x][y] += 1
                            avg[x][y] += s // 9
                j += 1

        return [[image[i][j] if cnt[i][j] == 0 else avg[i][j] // cnt[i][j] for j in range(m)] for i in range(n)]


s = Solution()
examples = [
    (dict(image=[[5, 6, 7, 10], [8, 9, 10, 10], [11, 12, 13, 10]], threshold=3),
     [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]),
    (dict(image=[[10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45]], threshold=12),
     [[25, 25, 25], [27, 27, 27], [27, 27, 27], [30, 30, 30]]),
    (dict(image=[[5, 6, 7], [8, 9, 10], [11, 12, 13]], threshold=1), [[5, 6, 7], [8, 9, 10], [11, 12, 13]]),
    (dict(image=[[0,3,8],[5,0,0],[3,7,2]], threshold=4), []),
]
for e, a in examples:
    print(a, e)
    print(s.resultGrid(**e))
