# 3033 修改矩阵
# https://leetcode.cn/problems/modify-the-matrix/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        mx = [max(col) for col in zip(*matrix)]
        return [[mx[j] if x == -1 else x for j, x in enumerate(row)] for i, row in enumerate(matrix)]
# leetcode submit region end(Prohibit modification and deletion)
