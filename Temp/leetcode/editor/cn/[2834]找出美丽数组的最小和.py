# 2834 找出美丽数组的最小和
# https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def minimumPossibleSum(self, n: int, target: int) -> int:
#         m = target // 2
#         # print(m,target+n-m+1)
#         # print(sum(range(1,m+1)),sum(range(target,target+n-m)))
#         if m < n:
#             return ((1+m)*m//2 + (target+target+n-m-1)*(n-m)//2) % (10**9+7)
#         else:
#             return (1+n)*n//2 % (10**9+7)
class Solution:
    def minimumPossibleSum(self, n: int, k: int) -> int:
        m = min(k // 2, n)
        return (m * (m + 1) + (k * 2 + n - m - 1) * (n - m)) // 2 % 1_000_000_007

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/solutions/2413304/o1-shu-xue-gong-shi-pythonjavacgo-by-end-xsxg/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# leetcode submit region end(Prohibit modification and deletion)
