# 1738 找出第 K 大的异或坐标值
# https://leetcode.cn/problems/find-kth-largest-xor-coordinate-value/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        rows = [list(accumulate(row, lambda x, y: x ^ y)) for row in matrix]
        for i in range(1, m):
            for j in range(n):
                rows[i][j] ^= rows[i - 1][j]
        a = sorted([x for row in rows for x in row], reverse=True)
        return a[k - 1]
# leetcode submit region end(Prohibit modification and deletion)
