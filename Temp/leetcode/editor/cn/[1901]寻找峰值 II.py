# 1901 寻找峰值 II
# https://leetcode.cn/problems/find-a-peak-element-ii/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        left, right = 0, n - 2
        while left <= right:
            mid = (left + right) // 2
            # 用这一行的最大值去和它相邻两行的同一列进行比较
            # 即满足了是第 mid 行峰顶
            mx = max(mat[mid])
            mx_i = mat[mid].index(mx)

            if mx > mat[mid + 1][mx_i]:
                right = mid - 1
            else:
                left = mid + 1
        # 最终 left 是峰顶所在的行
        return [left, mat[left].index(max(mat[left]))]

# leetcode submit region end(Prohibit modification and deletion)
