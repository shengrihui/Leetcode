# 3171 找到按位或最接近 K 的子数组
# https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        N = max(nums).bit_length()
        # bits[0/1][j] 子数组第 j 位 0/1 的数量
        bits = [[0] * N for _ in range(2)]
        left = 0
        ans = 10 ** 9

        def update(x, add):
            # 计算子数组或的结果
            ret = 0
            for j in range(N):
                bits[x >> j & 1][j] += add
                if bits[1][j] > 0:  # 只要有 1 就行 （题目是 与 的话还要不能有 0）
                    ret |= 1 << j
            return ret

        for right, x in enumerate(nums):
            s = update(x, 1)  # 往 bits 里加
            ans = min(ans, abs(k - s))
            # 越或越大，移动左端点 s 越小
            # 当 s >= k 移动 left （题目是 与 的话就 k >=s )
            while left < right and k <= s:
                s = update(nums[left], -1)  # 往 bits 里减少
                ans = min(ans, abs(k - s))
                left += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
