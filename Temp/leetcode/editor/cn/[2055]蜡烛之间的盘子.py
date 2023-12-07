# 2055 蜡烛之间的盘子
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        left = [0] * n  # left[i]，查询 i 的时候，i左边的蜡烛位置
        right = [n - 1] * n  # 同上
        pre_sum = [0] * n
        pre_sum[0] = int(s[0] == "*")
        for i in range(1, n):
            c = s[i]
            pre_sum[i] = pre_sum[i - 1] + (c == "*")
            left[i] = left[i - 1] if c == "*" else i
            ii = n - i - 1
            right[ii] = right[ii + 1] if s[ii] == "*" else ii
        ans = []
        for l, r in queries:
            r = pre_sum[left[r]] - pre_sum[right[l]]
            ans.append(r if r >= 0 else 0)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
