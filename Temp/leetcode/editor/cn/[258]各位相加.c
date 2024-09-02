// 258 各位相加
// https://leetcode.cn/problems/add-digits/


//leetcode submit region begin(Prohibit modification and deletion)
int addDigits(int num) {
    while (num >= 10) {
        int s = 0;
        while (num) {
            s += num % 10;
            num /= 10;
        }
        num = s;
    }
    return num;
}
//leetcode submit region end(Prohibit modification and deletion)
