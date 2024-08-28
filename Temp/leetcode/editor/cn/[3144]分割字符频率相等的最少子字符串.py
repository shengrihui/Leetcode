# 3144 分割字符频率相等的最少子字符串
# https://leetcode.cn/problems/minimum-substring-partition-of-equal-character-frequency/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            cnt = defaultdict(int)
            max_cnt = 0
            res = inf
            # [j...i] 是平衡的
            # 有 len(cnt) 个字符，平衡的话，len(cnt) * max(cnt.values()) == i-j+1
            for j in range(i, -1, -1):
                cnt[s[j]] += 1
                # max_cnt = max(max_cnt, cnt[s[j]])
                max_cnt = max_cnt if max_cnt > cnt[s[j]] else cnt[s[j]]
                if i - j + 1 == max_cnt * len(cnt):
                    # res = min(res, dfs(j - 1)+1)
                    r = dfs(j - 1) + 1
                    res = res if res < r else r
            return res

        return dfs(len(s) - 1)
# leetcode submit region end(Prohibit modification and deletion)
