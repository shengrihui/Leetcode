# 2866 美丽塔 II
# https://leetcode.cn/problems/beautiful-towers-ii/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        
        pre = [0] * n # pre[i] i 作为山顶它前面（不包括 i ）高度和
        st = [] # 存下标 
        for i,h in enumerate(maxHeights):
            while st and maxHeights[st[-1]] > h :
                st.pop()
            st.app---------:end(i)
# leetcode submit region end(Prohibit modification and deletion)
