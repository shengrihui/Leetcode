# 2024 考试的最大困扰度
# https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def f(ch: str) -> int:
            left = ans = cnt = 0
            for right, c in enumerate(answerKey):
                cnt += c != ch
                while cnt > k:
                    cnt -= answerKey[left] != ch
                    left += 1
                ans = max(ans, right - left + 1)
            return ans

        return max(f("T"), f("F"))
# leetcode submit region end(Prohibit modification and deletion)
