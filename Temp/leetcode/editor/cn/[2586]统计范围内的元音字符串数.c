// 2586 统计范围内的元音字符串数
// https://leetcode.cn/problems/count-the-number-of-vowel-strings-in-range/


//leetcode submit region begin(Prohibit modification and deletion)
bool isVowel(char ch) {
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
}
int vowelStrings(char** words, int wordsSize, int left, int right) {
    int ans = 0;
    for (int i = left; i <= right; i++) {
        ans += isVowel(words[i][0]) && isVowel(words[i][strlen(words[i]) - 1]);
    }
    return ans;
}
//leetcode submit region end(Prohibit modification and deletion)
