// 2024 考试的最大困扰度
// https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/

// leetcode submit region begin(Prohibit modification and deletion)
#define MAX(a, b) ((a) > (b) ? (a) : (b))
int f(char ch, int k, const char *s)
{
    int ans = 0, cnt = 0, left = 0;
    int n = strlen(s);
    for (int right = 0; right < n; right++)
    {
        cnt += s[right] != ch;
        while (cnt > k)
        {
            cnt -= s[left++] != ch;
        }
        ans = MAX(ans, right - left + 1);
    }
    return ans;
}

int maxConsecutiveAnswers(char *answerKey, int k)
{
    return MAX(f('T', k, answerKey), f('F', k, answerKey));
}
// leetcode submit region end(Prohibit modification and deletion)
