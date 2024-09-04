// 3174 清除数字
// https://leetcode.cn/problems/clear-digits/

//leetcode submit region begin(Prohibit modification and deletion)
char* clearDigits(char* s) {
    int top = 0; // 栈顶，指向接下来要填的位置
    for (int i = 0; s[i]; i++) {
        if (isdigit(s[i])) {
            top--; // 出栈
        } else {
            s[top++] = s[i]; // 入栈
        }
    }
    s[top] = '\0';
    return s;
}
//leetcode submit region end(Prohibit modification and deletion)
