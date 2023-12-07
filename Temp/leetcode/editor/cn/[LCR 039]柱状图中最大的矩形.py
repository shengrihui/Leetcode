# LCR 039 柱状图中最大的矩形
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [-1]
        ans = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while len(st) != 1 and heights[st[-1]] > h:
                j = st.pop()  # 栈顶（下标）
                hj = heights[j]  # 对顶的高度
                left = st[-1]  # 刚刚出战的高度往左最远能到的位置
                ans = max(ans, hj * (i - left - 1))
            st.append(i)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
