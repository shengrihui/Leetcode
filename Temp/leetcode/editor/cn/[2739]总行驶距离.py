# 2739 总行驶距离
# https://leetcode.cn/problems/total-distance-traveled/


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
#         ans = 0
#         while True:
#             d, r = divmod(mainTank, 5)
#             if d == 0:
#                 ans += r * 10
#                 break
#             ans += d * 50
#             add = min(additionalTank, d)
#             mainTank = r + add
#             additionalTank -= add
#         return ans

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        return (mainTank + min((mainTank - 1) // 4, additionalTank)) * 10
# leetcode submit region end(Prohibit modification and deletion)
