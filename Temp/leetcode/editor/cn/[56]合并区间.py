# 56 合并区间
from itertools import *
from typing import *


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
