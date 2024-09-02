// 263 丑数
// https://leetcode.cn/problems/ugly-number/


//leetcode submit region begin(Prohibit modification and deletion)
bool isUgly(int n) {
    if (n <= 0)return false;
    int a[3] = {2, 3, 5};
    for (int i = 0; i < 3; i++) {
        int x = a[i];
        while (n % x == 0)
            n /= x;
    }
    return n == 1;
}
//leetcode submit region end(Prohibit modification and deletion)
