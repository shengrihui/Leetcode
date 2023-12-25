# 1006 笨阶乘
# https://leetcode.cn/problems/clumsy-factorial/
from math import gcd


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def clumsy(self, n: int) -> int:
#         ops = ["*", "//", "+", "-"]
#         exp = []
#         op = 0
#         for i in range(n, 1, -1):
#             exp.append(str(i))
#             exp.append(ops[op % 4])
#             op += 1
#         exp.append("1")
#         return eval("".join(exp))

# class Solution:
#     def clumsy(self, n: int) -> int:
#         st = [n]
#         idx = 0
#         for i in range(n - 1, 0, -1):
#             if idx % 4 == 0:  # 乘，直接修改栈顶
#                 st[-1] *= i
#             elif idx % 4 == 1:  # 地板除，直接修改栈顶
#                 t = abs(st[-1]) // i
#                 st[-1] = -t if st[-1] < 0 else t
#             elif idx % 4 == 2:  # 加，入栈
#                 # st.append(i)
#                 # 在这道题里面，只有乘除加减而且是按顺序的
#                 # 所以加可以直接与栈顶计算
#                 st[-1] += i
#             elif idx % 4 == 3:  # 减，相反数入栈，可以最后直接求和
#                 st.append(-i)
#             idx += 1
#         return sum(st)


class Solution:
    def clumsy(self, n: int) -> int:
        # a = [0, 1, 2, 6, 7]
        # b = [1, 2, -1, -1]
        # if n <= 4: return a[n]
        # return n + b[n % 4]
        return n + [1, 2, 2, -1][n % 4] if n > 4 else [0, 1, 2, 6, 7][n]
# leetcode submit region end(Prohibit modification and deletion)
