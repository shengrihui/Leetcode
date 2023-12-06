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

# 给你一个由字符 'a'、'b'、'c' 组成的字符串 s 和一个非负整数 k 。每分钟，你可以选择取走 s 最左侧 还是 最右侧 的那个字符。 
# 
#  你必须取走每种字符 至少 k 个，返回需要的 最少 分钟数；如果无法取到，则返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aabaaaacaabc", k = 2
# 输出：8
# 解释：
# 从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。
# 从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。
# 共需要 3 + 5 = 8 分钟。
# 可以证明需要的最少分钟数是 8 。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a", k = 1
# 输出：-1
# 解释：无法取到一个字符 'b' 或者 'c'，所以返回 -1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s 仅由字母 'a'、'b'、'c' 组成 
#  0 <= k <= s.length 
#  
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 35 👎 0
