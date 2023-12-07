# 2520 统计能整除数字的位数


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        x = num
        while num:
            r = num % 10
            if x % r == 0:
                ans += 1
            num //= 10
        return ans
# leetcode submit region end(Prohibit modification and deletion)
