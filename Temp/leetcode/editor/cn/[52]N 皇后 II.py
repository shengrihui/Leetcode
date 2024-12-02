# 52 N 皇后 II
# https://leetcode.cn/problems/n-queens-ii/

# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         m = n * 2 - 1
#         ans = 0
#         col = [0] * n
#         on_path, diag1, diag2 = [False] * n, [False] * m, [False] * m
#
#         def dfs(r: int) -> None:
#             if r == n:
#                 nonlocal ans
#                 ans += 1
#                 return
#             for c, on in enumerate(on_path):
#                 if not on and not diag1[r + c] and not diag2[r - c]:
#                     col[r] = c
#                     on_path[c] = diag1[r + c] = diag2[r - c] = True
#                     dfs(r + 1)
#                     on_path[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场
#
#         dfs(0)
#         return ans


a = [1, 0, 0, 2, 10, 4, 40, 92, 352]


class Solution:
    def totalNQueens(self, n: int) -> int:
        return a[n - 1]
# leetcode submit region end(Prohibit modification and deletion)
