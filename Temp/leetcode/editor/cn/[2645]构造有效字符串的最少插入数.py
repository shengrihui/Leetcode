# 2645 构造有效字符串的最少插入数
# https://leetcode.cn/problems/minimum-additions-to-make-valid-string/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 贪心
    """
    def addMinimum(self, word: str) -> int:
        i = ans = 0
        s = "abc"
        for c in word:
            while c != s[i % 3]:
                ans += 1  # 该位置应该是 s[i % 3] 但不是所以要添加一个
                i += 1
            i += 1
        # return ans + abs((ord(word[-1]) - ord("c")))  # 末尾还要添加的数量
        return ans + {"a": 2, "b": 1, "c": 0}[word[-1]]
    """

    # DP
    """
    def addMinimum(self, word: str) -> int:
        n = len(word)
        dp = [0] * n
        # word[i] 比 word[i-1] 小或者相等，不管是 ca cb ba aa bb cc ，都是新的一组
        # dp[i] = dp[i-1] + 2
        # word[i] 比 word[i-1] 大，不管是 ab ac bc ，都是在同一组，要插入的数量上一个少 1
        # dp[i] = dp[i-1] - 1
        # 初始 dp[0]=2
        dp[0] = 2
        for i in range(1, n):
            dp[i] = dp[i - 1] + (2 if word[i] <= word[i - 1] else -1)
        return dp[-1]
    """

    # DP 改
    """
    def addMinimum(self, word: str) -> int:
        n = len(word)
        ans = 2
        for i in range(1, n):
            ans += 2 if word[i] <= word[i - 1] else -1
        return ans
    """

    # 一行
    def addMinimum(self, word: str) -> int:
        # return 2 + sum(2 if y <= x else -1 for x, y in pairwise(word))
        # return 2 + sum(2 if word[i] <= word[i - 1] else -1 for i in range(1, len(word)))
        return (1 + sum(word[i] <= word[i - 1] for i in range(1, len(word)))) * 3 - len(word)
# leetcode submit region end(Prohibit modification and deletion)
