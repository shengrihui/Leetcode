# 1534 统计好三元组
# https://leetcode.cn/problems/count-good-triplets/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):
                        ans += abs(arr[i] - arr[k]) <= c and abs(arr[k] - arr[j]) <= b
        return ans
    # leetcode submit region end(Prohibit modification and deletion)
