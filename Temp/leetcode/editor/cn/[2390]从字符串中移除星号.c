// 2390 从字符串中移除星号
// https://leetcode.cn/problems/removing-stars-from-a-string/


//leetcode submit region begin(Prohibit modification and deletion)
char* removeStars(char* s) {
    int i = 0, j = 0;
    for (; s[i]; i++) {
        if (s[i] == '*')
            j--;
        else
            s[j++] = s[i];
    }
    s[j] = '\0';
    return s;
}
//leetcode submit region end(Prohibit modification and deletion)
