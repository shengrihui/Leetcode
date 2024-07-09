# 1051 高度检查器
# https://leetcode.cn/problems/height-checker/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(x != y for x, y in zip(heights, sorted(heights)))
# leetcode submit region end(Prohibit modification and deletion)
