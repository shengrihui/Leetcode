# 1503 所有蚂蚁掉下来前的最后一刻
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left.append(0)
        right.append(n)
        return max(max(left), n - min(right))
# leetcode submit region end(Prohibit modification and deletion)
