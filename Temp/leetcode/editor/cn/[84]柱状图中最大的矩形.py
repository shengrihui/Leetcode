# 84 柱状图中最大的矩形
# https://leetcode.cn/problems/largest-rectangle-in-histogram/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
"""
# left[i] 和 right[i] 存 height[i] = h 左边和右边最近的的比 h 小的数的下标
# 这样，将 h 作为高度，(l,r) 可以作为宽度
# st 是单调递减栈 h <= st[-1] 的时候 pop
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        st = []
        for i, h in enumerate(heights):
            while st and h <= heights[st[-1]]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)

        right = [n] * n
        st = []
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while st and h <= heights[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        ans = 0
        for h, l, r in zip(heights, left, right):
            ans = max(ans, (r - l - 1) * h)
        return ans
"""


# 一次遍历
# 每次弹出的饿时候都计算面积
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = heights[0]
        heights.append(0)
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                leftIdx = stack[-1] if stack else -1
                result = max(result, heights[idx] * (i - leftIdx - 1))
            stack.append(i)
        return result

# leetcode submit region end(Prohibit modification and deletion)
