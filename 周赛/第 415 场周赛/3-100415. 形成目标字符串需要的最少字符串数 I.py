# 第 415 场周赛 第 3 题
# 题目：100415. 形成目标字符串需要的最少字符串数 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-415/problems/minimum-number-of-valid-strings-to-form-target-i/
# 题库：https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-i


# 超时
"""
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        st = set()
        for w in words:
            for i in range(1, len(w) + 1):
                st.add(w[:i])

        @cache
        def dfs(i: int) -> int:
            if i == n:
                return 0
            res = n - i
            for j in range(i, n):
                if target[i:j + 1] in st:
                    r = dfs(j + 1)
                    res = r if r < res else res
                else:
                    return res + 1 if res != n - i else n + 1
            return res + 1

        n = len(target)
        ans = dfs(0)
        return ans if ans <= n else -1
"""

s = Solution()
examples = [
    (dict(words=["b", "ccacc", "a"], target="cccaaaacba"), 8),
    (dict(words=["abc", "aaaaa", "bcdef"], target="aabcdabc"), 3),
    (dict(words=["abababab", "ab"], target="ababaababa"), 2),
    (dict(words=["abcdef"], target="xyz"), -1),
]
for e, a in examples:
    print(a, e)
    print(s.minValidStrings(**e))
