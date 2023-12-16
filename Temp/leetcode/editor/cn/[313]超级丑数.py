# 313 超级丑数
# https://leetcode.cn/problems/super-ugly-number/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
# 堆1
"""
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1
        ugly = primes.copy()
        se = set(primes)
        for _ in range(n - 2):
            u = heapq.heappop(ugly)
            for p in primes:
                pu = p * u
                if pu not in se:
                    se.add(pu)
                    heapq.heappush(ugly, p * u)
        return heapq.heappop(ugly)
"""


# 堆2
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        for _ in range(n - 1):
            u = heapq.heappop(ugly)
            for p in primes:
                heapq.heappush(ugly, u * p)
                if u % p == 0: break
        return heapq.heappop(ugly)

# 多路归并
# ans[i] * p 也是丑数
# 从 ans 中取出 anx[idx_p] * p 得到新的丑数
# 这么乘出来的结果，要么比 ans[-1] 大，直接加入，或者和它一样大，跳过它，直接让 idx_p+1
# class Solution:
#     def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
#         ans = [1]
#         q = [(p, p, 0) for p in primes]
#         while len(ans) < n:
#             ugly, p, idx = heapq.heappop(q)
#             if ugly != ans[-1]:
#                 ans.append(ugly)
#             heapq.heappush(q, (ans[idx + 1] * p, p, idx + 1))
#         return ans[-1]

# https://leetcode.cn/problems/super-ugly-number/solutions/924926/dong-tai-gui-hua-java-by-liweiwei1419-1yna/
# 动态规划（和上面三叶的多路归并很像）
# class Solution:
#     def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
#         dp = [inf] * n
#         dp[0] = 1
#         indies = [0] * len(primes)
#         for i in range(1, n):
#             for idx, p in zip(indies, primes):
#                 dp[i] = min(dp[i], dp[idx] * p)
#             for j, (idx, p) in enumerate(zip(indies, primes)):
#                 if dp[idx] * p <= dp[i]:
#                     indies[j] += 1
#         return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)
