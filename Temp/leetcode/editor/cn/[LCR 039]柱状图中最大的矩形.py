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


# 给定非负整数数组 heights ，数组中的数字用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入： heights = [2,4]
# 输出： 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= heights.length <=10⁵ 
#  0 <= heights[i] <= 10⁴ 
#  
# 
#  
# 
#  
#  注意：本题与主站 84 题相同： https://leetcode-cn.com/problems/largest-rectangle-in-
# histogram/ 
# 
#  Related Topics 栈 数组 单调栈 👍 108 👎 0
