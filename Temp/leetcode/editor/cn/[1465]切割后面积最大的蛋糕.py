# 1465 切割后面积最大的蛋糕
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        mxh = max(horizontalCuts[0], h - horizontalCuts[-1])
        mxv = max(verticalCuts[0], w - verticalCuts[-1])
        for x, y in pairwise(horizontalCuts):
            if y - x > mxh:
                mxh = y - x
        for x, y in pairwise(verticalCuts):
            if y - x > mxv:
                mxv = y - x
        return mxh * mxv % (10 ** 9 + 7)
# leetcode submit region end(Prohibit modification and deletion)


# 矩形蛋糕的高度为 h 且宽度为 w，给你两个整数数组 horizontalCuts 和 verticalCuts，其中： 
# 
#  
#  horizontalCuts[i] 是从矩形蛋糕顶部到第 i 个水平切口的距离 
#  verticalCuts[j] 是从矩形蛋糕的左侧到第 j 个竖直切口的距离 
#  
# 
#  请你按数组 horizontalCuts 和 verticalCuts 中提供的水平和竖直位置切割后，请你找出 面积最大 的那份蛋糕，并返回其 面积 。由
# 于答案可能是一个很大的数字，因此需要将结果 对 10⁹ + 7 取余 后返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
# 输出：4 
# 解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色的那份蛋糕面积最大。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
# 输出：6
# 解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色和黄色的两份蛋糕面积最大。 
# 
#  示例 3： 
# 
#  
# 输入：h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= h, w <= 10⁹ 
#  1 <= horizontalCuts.length <= min(h - 1, 10⁵) 
#  1 <= verticalCuts.length <= min(w - 1, 10⁵) 
#  1 <= horizontalCuts[i] < h 
#  1 <= verticalCuts[i] < w 
#  题目数据保证 horizontalCuts 中的所有元素各不相同 
#  题目数据保证 verticalCuts 中的所有元素各不相同 
#  
# 
#  Related Topics 贪心 数组 排序 👍 64 👎 0
