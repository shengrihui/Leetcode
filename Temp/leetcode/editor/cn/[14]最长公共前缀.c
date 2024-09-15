// 14 最长公共前缀
// https://leetcode.cn/problems/longest-common-prefix/

//leetcode submit region begin(Prohibit modification and deletion)
char* longestCommonPrefix(char** strs, int strsSize) {
    char* s0 = strs[0];
    for (int j = 0; j < strlen(s0); j++) {
        for (int i = 0; i < strsSize; i++) {
            char* s = strs[i];
            // strs[i] 长度不足 j 或者 strs[i] 的第 j 位与 s0 的第 j 位不同
            if (strlen(s) == j || s[j] != s0[j]) {
                s0[j] = '\0';
                return s0;
            }
        }
    }
    return s0;
}
//leetcode submit region end(Prohibit modification and deletion)
