# 682 棒球比赛
# https://leetcode.cn/problems/baseball-game/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for op in operations:
            if op == "C":
                st.pop()
            elif op == "D":
                st.append(st[-1] * 2)
            elif op == "+":
                st.append(st[-1] + st[-2])
            else:
                st.append(int(op))
        return sum(st)
# leetcode submit region end(Prohibit modification and deletion)
