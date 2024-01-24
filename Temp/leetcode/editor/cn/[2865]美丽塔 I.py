# 2865 美丽塔 I
# https://leetcode.cn/problems/beautiful-towers-i/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        st = [-1]
        left_sum = [0] * n
        for i, x in enumerate(maxHeights):
            while len(st) > 1 and x <= maxHeights[st[-1]]:
                st.pop()
            left_sum[i] = left_sum[st[-1]] + (i - st[-1]) * x  # 包括 i
            st.append(i)

        st = [n]
        ans = 0
        right_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            x = maxHeights[i]
            while len(st) > 1 and x <= maxHeights[st[-1]]:
                st.pop()
            right_sum[i] = right_sum[st[-1]] + (st[-1] - i) * x  # 包括 i
            st.append(i)
            ans = max(ans, right_sum[i] + left_sum[i] - x)
        return ans

# class Solution:
#     def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
#         n = len(maxHeights)
#         suf = [maxHeights[-1]] * n
#         st = [n]  # 将n作为栈底，为了计算个数方便，计算 maxHeights[st[1]] 的个数方便
#         s = 0
#         for i in range(n - 1, -1, -1):
#             x = maxHeights[i]  # 第i个值
#             while len(st) > 1 and x <= maxHeights[st[-1]]:
#                 j = st.pop()  # 将大于等于 x 的 下标（存的是下标） 都弹出
#                 s -= (st[-1] - j) * maxHeights[j]  # 把 [j,st[-1]) 之间的值先减掉，值是 maxHeights[j]
#             st.append(i)  # 入栈
#             s += (st[-2] - i) * x
#             suf[i] = s
#
#         ans = suf[0]
#
#         # pre = [0] * n
#         st = [-1]  # 将n作为栈底，为了计算个数方便，计算 maxHeights[st[1]] 的个数方便
#         s = 0
#         for i in range(n):
#             x = maxHeights[i]
#             while len(st) > 1 and x <= maxHeights[st[-1]]:
#                 j = st.pop()  # 将大于等于 x 的 下标（存的是下标） 都弹出
#                 s -= (j - st[-1]) * maxHeights[j]  # 把 [j,st[-1]) 之间的值先减掉，值是 maxHeights[j]
#             st.append(i)  # 入栈
#             s += (i - st[-2]) * x
#             # pre[i] = s
#             ans = max(ans, s + suf[i] - maxHeights[i])
#
#         return ans

# leetcode submit region end(Prohibit modification and deletion)
