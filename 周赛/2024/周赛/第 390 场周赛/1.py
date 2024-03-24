# https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/description/
from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = left = 0
        cnt = Counter()
        for i, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 2:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans
