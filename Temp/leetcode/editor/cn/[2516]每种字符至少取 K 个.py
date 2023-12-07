# 2516 每种字符至少取 K 个
from collections import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        cnt = Counter(s)
        if k == 0:
            return 0
        if any(c not in cnt or cnt[c] < k for c in "abc"):  # 存在一个字符的数量没有到 k ，返回 -1
            return -1
        right = n
        d = {c: 0 for c in "abc"}
        # 后缀，移动 right 直到 abd 的数量都至少为 k
        while right and any(v < k for v in d.values()):
            right -= 1
            d[s[right]] += 1
        ans = n - right
        left = 0
        while left <= right:  # 可以等于，当等于的时候，一定会启动里面这个 while，并更新 ans
            ch = s[left]
            d[ch] += 1
            while right < n and d[s[right]] - 1 >= k:
                d[s[right]] -= 1
                right += 1
            ans = min(ans, left + 1 + n - right)
            if right == n:  # 前缀已经满足“至少”
                break
            left += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
"""
"bcca"
1

"""
s = Solution()
# print(s.takeCharacters("aabaaaacaabc", 2))
print(s.takeCharacters("bcca", 1))
