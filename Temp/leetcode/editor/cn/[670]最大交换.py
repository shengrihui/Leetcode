# 670 最大交换
# https://leetcode.cn/problems/maximum-swap/


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def maximumSwap(self, num: int) -> int:
#         ans = num
#         s = list(str(num))
#         n = len(s)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 s[i], s[j] = s[j], s[i]
#                 ans = max(ans, int("".join(s)))
#                 s[i], s[j] = s[j], s[i]
#         return ans
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        t = list(str(num))
        t.sort(reverse=True)  # 降序排序
        for i, (x, y) in enumerate(zip(s, t)):
            if x != y:  # t 降序，如果不一样了那这一位交换
                j = len(t) - 1 - (s[::-1]).index(y)  # 在 s 从右往左找到 y ，是另一个交换的位置
                s[i], s[j] = s[j], s[i]
                return int("".join(s))
        return num
# leetcode submit region end(Prohibit modification and deletion)
