# 3164 优质数对的总数 II
# https://leetcode.cn/problems/find-the-number-of-good-pairs-ii/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# 统计因子（站在 nums1 的角度）
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt = defaultdict(int)
        for x in nums1:
            if x % k != 0:  # x 不是 k 的倍数
                continue
            # 枚举 x // k 的因子
            x //= k
            for i in range(1, isqrt(x) + 1):
                # i 和 x // i 是 x//k 的因子
                if x % i == 0:
                    cnt[i] += 1
                    if i * i < x:
                        cnt[x // i] += 1
        # 枚举 nums2[i] = y，将 y 看做因子统计 cnt[y]
        # 也就是 nums1 中有多少个数是 y * k 的倍数
        return sum(cnt[y] for y in nums2)


# 统计倍数（站在 nums2 的角度）
# nums2 中的每个数的各个倍数的 k 倍在 nums1 中出现了多少次
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 统计 nums1 中 x // k 出现多少次
        cnt1 = Counter(x // k for x in nums1 if x % k == 0)
        if not cnt1:
            return 0
        ans = 0
        cnt2 = Counter(nums2)  # 避免重复计算相同的数
        u = max(nums1)
        for y, c in cnt2.items():
            s = 0
            for d in range(y, u + 1, y):  # 遍历 y 的倍数
                s += cnt1[d]
            ans += s * c
        return ans
# leetcode submit region end(Prohibit modification and deletion)
