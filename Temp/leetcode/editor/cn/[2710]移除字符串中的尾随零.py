# 2710 移除字符串中的尾随零
# https://leetcode.cn/problems/remove-trailing-zeros-from-a-string/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # for i in range(len(num) - 1, -1, -1):
        #     if num[i] != "0":
        #         return num[:i + 1]
        # return num
        return num.rstrip('0')
# leetcode submit region end(Prohibit modification and deletion)
