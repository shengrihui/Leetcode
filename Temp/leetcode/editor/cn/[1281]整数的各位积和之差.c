// 1281 整数的各位积和之差
// https://leetcode.cn/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


//leetcode submit region begin(Prohibit modification and deletion)


int subtractProductAndSum(int n) {
    int m = 1, s = 0;
    while (n) {
        int r = n % 10;
        m *= r;
        s += r;
        n /= 10;
    }
    return m - s;
}
//leetcode submit region end(Prohibit modification and deletion)
