# 56 合并区间
from typing import *
from collections import *
from itertools import *
from functools import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        diff = [0] * (max(x for _, x in intervals) + 2)
        ans = []
        for s, e in intervals:
            diff[s] += 1
            diff[e + 1] -= 1
        pre = list(accumulate(diff))
        s = 0
        print(diff)
        print(pre)
        for i in range(1, len(pre)):
            if pre[i] > 0 and pre[i - 1] == 0:
                s = i
            if pre[i] > 0 and pre[i + 1] == 0:
                ans.append([s, i])
        return ans


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for s, e in intervals:
            if s > ans[-1][1]:
                ans.append([s, e])
            else:
                ans[-1][1] = max(ans[-1][1], e)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.merge([[1, 4], [5, 6]]))

# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返
# 回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2： 
# 
#  
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= intervals.length <= 10⁴ 
#  intervals[i].length == 2 
#  0 <= starti <= endi <= 10⁴ 
#  
# 
#  Related Topics 数组 排序 👍 2099 👎 0
