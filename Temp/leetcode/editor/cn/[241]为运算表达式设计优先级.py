# 241 为运算表达式设计优先级
from itertools import *
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def dfs(exp: List[str]) -> List[int]:
            # 表达式 exp 的结果
            n = len(exp)
            if n == 1:
                return [int(exp[0])]
            ans = []
            for i in range(1, n, 2):  # exp[i] 是运算符
                l, r = dfs(exp[:i]), dfs(exp[i + 1:])  # 以 exp[i] 这个运算符分隔开的两边的表达式都能有怎样的结果
                op = exp[i]
                for a, b in product(l, r):
                    # 等价于
                    # for a in l:
                    #     for b in r:
                    if op == "+":
                        ans.append(a + b)
                    elif op == "-":
                        ans.append(a - b)
                    elif op == "*":
                        ans.append(a * b)
            return ans

        exp = []
        i, n = 0, len(expression)
        while i < n:
            start = i
            i = i + 1
            while i < n and expression[i] not in "+-*":
                i += 1
            exp.append(expression[start:i])  # 加入数字
            if i < n:
                exp.append(expression[i])  # 符号
                i += 1
        return dfs(exp)
# leetcode submit region end(Prohibit modification and deletion)
