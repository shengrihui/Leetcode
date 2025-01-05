# 2241 设计一个 ATM 机器
# https://leetcode.cn/problems/design-an-atm-machine/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class ATM:

    def __init__(self):
        self.cnt = [0] * 5
        self.acc = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, b in enumerate(banknotesCount):
            self.cnt[i] += b

    def withdraw(self, amount: int) -> List[int]:
        w = [0] * 5
        for i in range(4, -1, -1):
            acc = self.acc[i]
            x = min(amount // acc, self.cnt[i])
            w[i] += x
            amount -= x * acc
        if amount:
            return [-1]
        for i in range(5):
            self.cnt[i] -= w[i]
        return w
# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
# leetcode submit region end(Prohibit modification and deletion)
