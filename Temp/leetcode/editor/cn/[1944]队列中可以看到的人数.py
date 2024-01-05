# 1944 队列中可以看到的人数
# https://leetcode.cn/problems/number-of-visible-people-in-a-queue/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        st = []
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while st and heights[st[-1]] < h:
                ans[i] += 1  # i 右边多一个能看到
                st.pop()
            if st:  # heights[i] 右边第一个比他大的也能看到
                ans[i] += 1
            st.append(i)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
