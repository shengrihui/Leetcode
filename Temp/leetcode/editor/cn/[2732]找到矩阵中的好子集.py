# 2732 找到矩阵中的好子集
# https://leetcode.cn/problems/find-a-good-subset-of-the-matrix/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        def row2int(row: List[int]) -> int:
            res = 0
            for i, x in enumerate(reversed(row)):
                res |= x << i
            return res

        d = dict()
        vis = set()
        for i, row in enumerate(grid):
            x = row2int(row)
            if x == 0:
                return [i]
            if x in vis:
                continue
            if x in d:
                return [d[x], i]
            zeros = [i for i, x in enumerate(reversed(row)) if x == 0]
            good = [0]
            for z in zeros:
                for g in good.copy():
                    t = g | (1 << z)
                    good.append(t)
                    d[t] = i
            # print(row, x, d)
            vis.add(x)
        return []

# leetcode submit region end(Prohibit modification and deletion)
