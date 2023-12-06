class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        right = 0
        lookup = set()
        ans = 0
        while right < len(s):
            while s[right] in lookup:
                lookup.remove(s[left])  # 移除左边
                left += 1
            lookup.add(s[right])
            ans = max(ans, right - left)
            right += 1
        return ans + 1


s = Solution()
examples = [
    "abcabcbb",
    "bbbbb",
    "pwwkew"
]
for e in examples:
    print(e)
    print(s.lengthOfLongestSubstring(e))
