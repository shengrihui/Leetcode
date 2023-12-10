# 373 查找和最小的 K 对数字
# https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# 多路归并
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Memory Limit Exceeded
        # return sorted(list(product(nums1, nums2)), key=lambda x: x[0] + x[1])[:k]
        # 多路归并
        n, m = len(nums1), len(nums2)
        # 将 [nums1[i],nums2[0]] 入堆
        q = [(nums1[i] + nums2[0], i, 0) for i in range(n)]
        heapq.heapify(q)
        ans = []
        for _ in range(min(m * n, k)):
            s, i, j = heapq.heappop(q)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < m:
                heapq.heappush(q, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans


# 多次二分
# 超时
"""
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def check(mid: int) -> bool:
            cnt = 0
            for a in nums1:
                for b in nums2:
                    if a + b <= mid:
                        cnt += 1
                    else:
                        break
            return cnt > k

        n, m = len(nums1), len(nums2)
        if m * n <= k:  # 特判一下~
            return list(product(nums1, nums2))
        l, r = nums1[0] + nums2[0], nums2[-1] + nums2[-1]  # 数对的值域的两个端点
        # 在 [l,r] 中寻找 x，x 是第 k+1 个数
        # 也就是说，小于 x 的数有 k1 个，k1<=k，
        # 如果 k1==k ，可以返回答案了；
        # 如果 k1<k ，再向答案中加入一定量的数对和为 x 的数对
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        x = l

        ans = []
        indies = [m] * n  # indies[i] = j ： nums1[i] + nums2[j] >= x 的最小 j
        # 将数对和 < x 的加入答案
        for i, a in enumerate(nums1):
            for j, b in enumerate(nums2):
                if a + b < x:
                    ans.append([a, b])
                else:
                    indies[i] = j
                    break

        # 将数对和 == x 的加入答案，直到 len(ans)==k
        i = 0
        while i < n and len(ans) < k:
            j = indies[i]
            if j == m:
                i += 1
                continue
            b = x - nums2[j]
            while len(ans) < k and nums2[j] == b:
                ans.append([nums1[i], nums2[j]])
                j += 1
            i += 1
        return ans
"""
# leetcode submit region end(Prohibit modification and deletion)
