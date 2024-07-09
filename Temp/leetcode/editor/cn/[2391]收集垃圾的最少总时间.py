# 2391 收集垃圾的最少总时间
# https://leetcode.cn/problems/minimum-amount-of-time-to-collect-garbage/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        last = {"M": 0, "P": 0, "G": 0}
        ans = 0
        pre = list(accumulate(travel, initial=0))
        for i in range(n - 1, -1, -1):
            for m in "MPG":
                if last[m] == 0 and m in garbage[i]:
                    last[m] = i
                    ans += pre[i]
            ans += len(garbage[i])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
