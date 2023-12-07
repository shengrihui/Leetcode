# 2591 将钱分给最多的儿童


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:  # 没有任何方案
            return -1
        money -= children  # 每人都分1
        eight = money // 7  # 可以分到8美元的
        if eight > children or eight == children and money % 7:  # 每个人都能分到8美元后还有多都给一个人
            return children - 1
        if money % 7 == 3 and children - eight == 1:  # 只有一个人分到4美元
            return eight - 1
        return eight
    # leetcode submit region end(Prohibit modification and deletion)
