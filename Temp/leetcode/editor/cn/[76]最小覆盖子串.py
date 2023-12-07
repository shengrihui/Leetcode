# 76 最小覆盖子串
from collections import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 双指针/滑动歘口
        t_cnt = Counter(t)
        cnt = defaultdict(int)
        n = len(s)
        mn, mnl, mnr = n + 1, 0, 0
        left = 0
        for right, c in enumerate(s):
            cnt[c] += 1
            # 满足覆盖移动左指针
            while all(cnt[c] >= v for c, v in t_cnt.items()):
                # 当前长度更小了，更新答案的区间范围
                if mn > (t := right - left + 1):
                    mn, mnl, mnr = t, left, right
                cnt[s[left]] -= 1
                left += 1
        return "" if mn == n + 1 else s[mnl:mnr + 1]
# leetcode submit region end(Prohibit modification and deletion)
