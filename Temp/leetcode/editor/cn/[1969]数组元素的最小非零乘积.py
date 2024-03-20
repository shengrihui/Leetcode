# 1969 数组元素的最小非零乘积
# https://leetcode.cn/problems/minimum-non-zero-product-of-the-array-elements/


# leetcode submit region begin(Prohibit modification and deletion)
# 假设现在把 x 的 0 和 y 的 1 交换，位置是第 k 位
# 那么 y = y' + 2^k
# xy = x(y' + 2^k) = xy' + x*2^k
# 交换后
# x' = x + 2^k
# y'' = y'
# x'y' = (x + 2^k )y' = xy' + y'*2^k
# 所以，只要 x>y', 就可以这么操作使得乘积变小
# 也就是，找两个数，一个大一个小，且对应位置上不相同
# 那么就把一个使劲大，一个使劲小就可以了
# 方法是：
# 将 [1,2^p-1] 的最大先拿一边
# 剩下的最大和最小两两一组，做上面的操作
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 1_000_000_007
        k = (1 << p) - 1  # 最大的那个值
        return k * pow(k - 1, k >> 1, MOD) % MOD
# leetcode submit region end(Prohibit modification and deletion)
