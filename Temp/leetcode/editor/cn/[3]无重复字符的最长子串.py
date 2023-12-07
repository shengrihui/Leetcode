# 3 无重复字符的最长子串


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        windows = set()
        ans = 0
        for right, c in enumerate(s):
            while c in windows:  # 加入 c 之后有重复元素，移动左指针
                windows.remove(s[left])
                left += 1
            windows.add(c)
            ans = max(ans, right - left + 1)  # 当前子串长度更新 ans
        return ans


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        prior = [-1] * n  # 上一次出现的位置
        d = dict()
        for i, c in enumerate(s):
            if c in d:
                prior[i] = d[c]
            d[c] = i
        # print(d)
        # print(prior)

        l, r = 0, 1
        ans = 0
        while l <= r < n:
            if prior[r] < l:
                r += 1
            else:
                l = prior[r] + 1
            # print(l, r)
            ans = max(ans, r - l)

        return ans

# leetcode submit region end(Prohibit modification and deletion)
