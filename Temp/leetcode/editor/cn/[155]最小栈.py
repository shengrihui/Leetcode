# 155 最小栈
# https://leetcode.cn/problems/min-stack/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
"""
# 一个栈，记录 (val, min)
class MinStack:

    def __init__(self):
        self.st = [(inf, inf)]

    def push(self, val: int) -> None:
        self.st.append((val, val if val < self.st[-1][1] else self.st[-1][1]))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
"""


class MinStack:

    def __init__(self):
        self.st = []
        self.mn = inf

    def push(self, val: int) -> None:
        self.st.append(val - self.mn)
        if val < self.mn:
            self.mn = val

    def pop(self) -> None:
        x = self.st.pop()
        if x < 0:
            # 推导：
            # x > 0 对 mn 没有影响
            # 只有 val < old_mn
            # 即 val - old_mn = x < 0
            # 会修改 mn， new_mn = val
            # 那么
            # old_mn = val - x = new_mn - x
            self.mn -= x

    def top(self) -> int:
        x = self.st[-1]
        # 推导：
        # val 是原值，x 是栈顶现在存的元素
        # val - old_mn = x
        # if x < 0:
        #     new_mn = val
        #
        #     val = new_mn
        # else:
        #     new_mn = old_mn
        #
        #     val = x + new_mn
        return self.mn if x < 0 else x + self.mn

    def getMin(self) -> int:
        return self.mn
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
