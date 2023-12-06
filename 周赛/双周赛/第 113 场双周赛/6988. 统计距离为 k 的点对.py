from typing import List
from collections import *
from itertools import *

# 题目：# 6988. 统计距离为 k 的点对
# 题目链接：https://leetcode.cn/problems/count-pairs-of-points-with-distance-k/
# class Solution:
#     def countPairs(self, coordinates: List[List[int]], k: int) -> int:
#         n = len(coordinates)
#         ans = 0
#         for i in range(n - 1):
#             x1, y1 = coordinates[i]
#             for j in range(i + 1, n):
#                 x2, y2 = coordinates[j]
#                 if (x1 ^ x2) + (y1 ^ y2) == k:
#                     ans += 1
#         return ans

"""
x1 ^ x2 = i
x1 ^ i = x2

(x1 ^ x2) + (y1 ^ y2) = k
y1 ^ y2 = k - i
y1 = (k - i) ^ y2

遍历所有点(x, y)，
对每个点遍历k的范围计算(x ^ i, (k - i) ^ y)
并将在之前遍历过的点中有多少这样结果的点的数量加到答案里
"""


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        ans = 0
        cnt = Counter()
        for x, y in coordinates:
            for i in range(k + 1):  # k的范围是[0,100]
                ans += cnt[x ^ i, y ^ (k - i)]
            cnt[x, y] += 1  # 因为要求x2>x1,所以在k循环后面加
        return ans


s = Solution()
examples = [
    (dict(coordinates=[[1, 2], [4, 2], [1, 3], [5, 2]], k=5), 2),
    # (dict(),),
]
for e, a in examples:
    print(a, e)
    print(s.countPairs(**e))
