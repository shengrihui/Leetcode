# 3 无重复字符的最长子串
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


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


# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 5 * 10⁴ 
#  s 由英文字母、数字、符号和空格组成 
#  
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 9803 👎 0
