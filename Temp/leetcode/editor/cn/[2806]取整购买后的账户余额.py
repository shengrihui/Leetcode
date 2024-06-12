# 2806 取整购买后的账户余额
# https://leetcode.cn/problems/account-balance-after-rounded-purchase/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        p, r = divmod(purchaseAmount, 10)
        return 100 - (p + (r >= 5)) * 10
    # leetcode submit region end(Prohibit modification and deletion)
