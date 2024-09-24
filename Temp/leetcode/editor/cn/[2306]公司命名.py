# 2306 公司命名
# https://leetcode.cn/problems/naming-a-company/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = defaultdict(set)
        for s in ideas:
            groups[s[0]].add(s[1:])
        ans = 0
        for A in groups.values():
            for B in groups.values():
                # 以 a 开头的字符串集合 A，以 b 开头的字符串集合 B
                # A 中取一个 B 中取一个组成答案，但两个都有的不能取
                # 再考虑先后顺序 * 2
                # 但又因为 A 和 B 的遍历顺序，会有重复的选择，最后 ans 还要 // 2
                # 所以最后直接
                m = len(A & B)  # 交际的大小
                ans += (len(A) - m) * (len(B) - m)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
