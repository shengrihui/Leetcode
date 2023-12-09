class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        prior = [-1] * n  # 记录第i个字符上一次出现在什么位置
        d = dict()  # d[c]=i，c这个字符上一次出现在i
        for i, c in enumerate(s):
            if c in d:
                prior[i] = d[c]
            d[c] = i  # 更新d[c]
        # print(d)
        # print(prior)

        l, r = 0, 1
        ans = 0
        while l <= r < n:
            if prior[r] < l:  # s[r]的上一次出现在l的前面，r继续右移
                r += 1
            else:  # 否则l移动到prior[r]的下一个
                l = prior[r] + 1
            # print(l, r)
            ans = max(ans, r - l)

        return ans


s = Solution()
examples = [
    "abcabcbb",
    "bbbbb",
    "pwwkew"
]
for e in examples:
    print(e, s.lengthOfLongestSubstring(e))
