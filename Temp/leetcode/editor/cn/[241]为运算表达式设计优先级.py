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


# 给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 按任意顺序 返回答案。 
# 
#  生成的测试用例满足其对应输出值符合 32 位整数范围，不同结果的数量不超过 10⁴ 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：expression = "2-1-1"
# 输出：[0,2]
# 解释：
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
#  
# 
#  示例 2： 
# 
#  
# 输入：expression = "2*3-4*5"
# 输出：[-34,-14,-10,-10,10]
# 解释：
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= expression.length <= 20 
#  expression 由数字和算符 '+'、'-' 和 '*' 组成。 
#  输入表达式中的所有整数值在范围 [0, 99] 
#  
# 
#  Related Topics 递归 记忆化搜索 数学 字符串 动态规划 👍 860 👎 0
