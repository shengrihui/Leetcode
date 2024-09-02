// 709 转换成小写字母
// https://leetcode.cn/problems/to-lower-case/


//leetcode submit region begin(Prohibit modification and deletion)
char* toLowerCase(char* s) {
    int n = strlen(s);
    for (int i = 0; i < n; i++) {
        if (s[i] >= 'A' && s[i] <= 'Z')
            s[i] += 32;
    }
    return s;
}
//leetcode submit region end(Prohibit modification and deletion)
