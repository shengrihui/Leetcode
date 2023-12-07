# 1423 可获得的最大点数
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 滑动窗口
        # 计算最小的的 n-k 个数
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        ss = sum(cardPoints)
        s = sum(cardPoints[:n - k])
        left = 0
        sk = s
        for right in range(n - k, n):
            s += cardPoints[right]
            s -= cardPoints[left]
            left += 1
            sk = min(s, sk)
        return ss - sk
# leetcode submit region end(Prohibit modification and deletion)
