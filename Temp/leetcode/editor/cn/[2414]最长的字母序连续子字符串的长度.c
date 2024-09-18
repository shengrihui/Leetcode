// 2414 最长的字母序连续子字符串的长度
// https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/


//leetcode submit region begin(Prohibit modification and deletion)
int longestContinuousSubstring(char* s) {
    int ans = 0, i = 0;
    while (s[i]) {
        int st = i++;
        while (s[i] && s[i] - s[i - 1] == 1)
            i++;
        ans = ans > i - st ? ans : i - st;
    }
    return ans;
}
//leetcode submit region end(Prohibit modification and deletion)
