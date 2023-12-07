# 2661 找出叠涂元素
from functools import *
from itertools import *
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        for ele in map(partial(map, {x: k for k, x in enumerate(arr)}.get), chain(mat, zip(*mat))):
            print(list(ele))
        return min(map(max, map(partial(map, {x: k for k, x in enumerate(arr)}.get), chain(mat, zip(*mat)))))
        # mn, m, n = len(arr), len(mat), len(mat[0])
        # mp = [[0, 0]] * (mn + 1)
        # for i, row in enumerate(mat):
        #     for j, x in enumerate(row):
        #         mp[x] = [i, j]
        # M, N = [n] * m, [m] * n
        # for idx, x in enumerate(arr):
        #     i, j = mp[x]
        #     M[i] -= 1
        #     N[j] -= 1
        #     if M[i] == 0 or N[j] == 0:
        #         return idx

# leetcode submit region end(Prohibit modification and deletion)
