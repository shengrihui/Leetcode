from typing import List
from collections import *
from itertools import *

# 题目：100049. 美丽塔 I
# 题目链接：
# 题目：100048. 美丽塔 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-364/problems/beautiful-towers-ii/
# 题库：https://leetcode.cn/problems/beautiful-towers-ii/

""""
单调栈核心
st = []
for x in a:
    while st and x <= a[st[-1]: # 不断将比 x 大的从栈中移出
        j = st.pop()
    st.append(i) 
"""


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        suf = [maxHeights[-1]] * n
        st = [n]  # 将n作为栈底，为了计算个数方便，计算 maxHeights[st[1]] 的个数方便
        s = 0
        for i in range(n - 1, -1, -1):
            x = maxHeights[i]  # 第i个值
            while len(st) > 1 and x <= maxHeights[st[-1]]:
                j = st.pop()  # 将大于等于 x 的 下标（存的是下标） 都弹出
                s -= (st[-1] - j) * maxHeights[j]  # 把 [j,st[-1]) 之间的值先减掉，值是 maxHeights[j]
            st.append(i)  # 入栈
            s += (st[-2] - i) * x
            suf[i] = s

        ans = suf[0]

        # pre = [0] * n
        st = [-1]  # 将n作为栈底，为了计算个数方便，计算 maxHeights[st[1]] 的个数方便
        s = 0
        for i in range(n):
            x = maxHeights[i]
            while len(st) > 1 and x <= maxHeights[st[-1]]:
                j = st.pop()  # 将大于等于 x 的 下标（存的是下标） 都弹出
                s -= (j - st[-1]) * maxHeights[j]  # 把 [j,st[-1]) 之间的值先减掉，值是 maxHeights[j]
            st.append(i)  # 入栈
            s += (i - st[-2]) * x
            # pre[i] = s
            ans = max(ans, s + suf[i] - maxHeights[i])

        return ans


s = Solution()
examples = [
    (dict(maxHeights=[5, 3, 4, 1, 1]), 13),
    (dict(maxHeights=[6, 5, 3, 9, 2, 7]), 22),
    (dict(maxHeights=[3, 2, 5, 5, 2, 3]), 18),
    (dict(maxHeights=[3, 6, 3, 5, 5, 1, 2, 5, 5, 6]), 24),
]
for e, a in examples:
    print(a, e)
    print(s.maximumSumOfHeights(**e))
