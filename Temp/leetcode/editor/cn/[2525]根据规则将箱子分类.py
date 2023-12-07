# 2525 根据规则将箱子分类


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        return [["Neither", "Heavy"], ["Bulky", "Both"]][
            length >= 10000 or width >= 10000 or height >= 10000 or length * width * height >= 10 ** 9][mass >= 100]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def categorizeBox(self, a, b, c, m, R=[["Neither", "Heavy"], ["Bulky", "Both"]], N=10000, M=10 ** 9) -> str:
        return R[a >= N or b >= N or c >= N or a * b * c >= M][m >= 100]

# leetcode submit region end(Prohibit modification and deletion)
