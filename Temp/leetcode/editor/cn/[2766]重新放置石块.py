# 2766 重新放置石块
# https://leetcode.cn/problems/relocate-marbles/
from imports import *


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        for f, t in zip(moveFrom, moveTo):
            if f != t:
                d[t] += d[f]
                d[f] = 0
        return sorted(i for i, v in d.items() if v > 0)


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        st = set(nums)
        for f, t in zip(moveFrom, moveTo):
            st.remove(f)
            st.add(t)
        return sorted(st)
# leetcode submit region end(Prohibit modification and deletion)
