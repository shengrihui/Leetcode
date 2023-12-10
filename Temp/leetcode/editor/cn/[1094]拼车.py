# 1094 拼车
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        a = [0] * 1001
        for n, f, t in trips:
            a[f] += n
            a[t] -= n
        if a[0] > capacity:
            return False
        for i in range(1, 1001):
            a[i] += a[i - 1]
            if a[i] > capacity:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
