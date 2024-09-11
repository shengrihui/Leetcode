# 2555 两个线段获得的最多奖品
# https://leetcode.cn/problems/maximize-win-from-two-segments/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        # 两个线段紧挨着但端点不重合的总长度能够覆盖所有奖品
        if k * 2 + 1 >= prizePositions[-1] - prizePositions[0]:
            return n
        # 定义 mx[i + 1] 表示线段的右端点为 i 的时候最多的奖品数
        # 枚举第二条线段的右端点 right，用滑窗计算出这条线段最远的 left
        # 记这个线段的长度为 size = right - left + 1
        # 更新 mx[right + 1] = max(mx[right], size)
        # 更新答案 ans = max(ans, size + mx[left])
        # 就是贪心地假设第二个线段的右端点在 right，第一条线段的右端点是 left - 1
        # 如果第一条线段前面长度不够 k 那就让这两个线段重合，反正每个奖品都只会计算一次
        # 两个更新顺序无所谓
        ans = left = 0
        mx = [0] * (n + 1)  # 因为 right 会到最后而且 k 可以是 0 所以 mx 长度简单设置为 n+1
        for right, p in enumerate(prizePositions):
            while p - prizePositions[left] > k:
                left += 1
            size = right - left + 1
            mx[right + 1] = max(mx[right], size)
            ans = max(ans, size + mx[left])
        return ans


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        # 两个线段紧挨着但端点不重合的总长度能够覆盖所有奖品
        if k * 2 + 1 >= prizePositions[-1] - prizePositions[0]:
            return n
        # 枚举中间 mid
        # mx 有点像上面的 mx[mid + 1]
        # 向右一次滑窗更新 ans = max(ans, mx + right - mid)
        # 也就是 [mid,right) 的 和 [left,mid) 这两个区间的奖品数量 right - mid 和 mx
        # 音效要先更新 ans ，不然更新后的 mx 对应的就是 [新left,mid] 了，mid 会算两边
        # 向左一次滑窗更新 mx
        mx = ans = left = right = 0
        for mid, p in enumerate(prizePositions):
            while right < n and prizePositions[right] - p <= k:
                right += 1
            # right 是右端点 +1 的位置
            ans = max(ans, mx + right - mid)
            while p - prizePositions[left] > k:
                left += 1
            mx = max(mx, mid - left + 1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
