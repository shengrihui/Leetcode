# 575 分糖果
# https://leetcode.cn/problems/distribute-candies/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        nn, m = len(candyType) // 2, len(set(candyType))
        return nn if m > nn else m
# leetcode submit region end(Prohibit modification and deletion)
