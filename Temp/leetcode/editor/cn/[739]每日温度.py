# 739 每日温度
# https://leetcode.cn/problems/daily-temperatures/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n - 1, -1, -1):
            t = temperatures[i]
            while st and temperatures[st[-1]] <= t:
                st.pop()
            if st:
                ans[i] = st[-1] - i
            st.append(i)
        return ans
"""


# 从前往后遍历，单调递减栈
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        st = []
        for i, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                j = st.pop()
                ans[j] = i - j
            st.append(i)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
