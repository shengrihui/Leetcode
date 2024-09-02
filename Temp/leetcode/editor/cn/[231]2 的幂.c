// 231 2 的幂
// https://leetcode.cn/problems/power-of-two/


//leetcode submit region begin(Prohibit modification and deletion)
int BIG = 1 << 30;
bool isPowerOfTwo(int n) {
        // return n > 0  && ((n & -n) == n);
        return n > 0 && BIG % n == 0;
}
//leetcode submit region end(Prohibit modification and deletion)
