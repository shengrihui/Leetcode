# 997 找到小镇的法官
# https://leetcode.cn/problems/find-the-town-judge/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cnt, cnt_ed = defaultdict(int), defaultdict(int)
        for a, b in trust:
            cnt_ed[b] += 1  # b 被信任的数量 +1
            cnt[a] += 1  # a 信任的数量 +1
        for i in range(1, n + 1):
            if cnt[i] == 0 and cnt_ed[i] == n - 1:
                return i
        return -1
# leetcode submit region end(Prohibit modification and deletion)
