# 1052 爱生气的书店老板
# https://leetcode.cn/problems/grumpy-bookstore-owner/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        ans = 0
        pre = [0] * (n + 1)
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            if g == 0:
                ans += c
                pre[i + 1] = pre[i]
            else:
                pre[i + 1] = pre[i] + c
        happy = 0
        for right in range(minutes, n + 1):
            happy = max(happy, pre[right] - pre[right - minutes])
        return ans + happy

# leetcode submit region end(Prohibit modification and deletion)
