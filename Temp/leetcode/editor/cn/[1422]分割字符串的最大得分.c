// 1422 分割字符串的最大得分
// https://leetcode.cn/problems/maximum-score-after-splitting-a-string/


//leetcode submit region begin(Prohibit modification and deletion)
#define MAX(a, b) ((a) > (b) ? (a) : (b))
int maxScore(char* s) {
    int n = strlen(s);
    int one = 0, zero = 0;
    for (int i = 0; i < n; i++)
        one += s[i] == '1';
    int ans = 0;
    for (int i = 0; i < n - 1; i++) {
        zero += s[i] == '0';
        one -= s[i] == '1';
        ans = MAX(ans, one + zero);
    }
    return ans;
}
//leetcode submit region end(Prohibit modification and deletion)
