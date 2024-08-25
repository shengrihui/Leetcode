# 第 412 场周赛 第 4 题
# 题目：100403. 统计近似相等数对 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-412/problems/count-almost-equal-pairs-ii/
# 题库：https://leetcode.cn/problems/count-almost-equal-pairs-ii

from collections import *
from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        nums.sort()
        ans = 0
        for x in nums:
            st = {x}  # 不交换
            s = list(str(x))
            m = len(s)
            for i in range(m):
                for j in range(i + 1, m):
                    s[i], s[j] = s[j], s[i]  # 一次交换
                    st.add(int("".join(s)))
                    for p in range(i + 1, m):
                        for q in range(p + 1, m):
                            s[p], s[q] = s[q], s[p]  # 第二次交换
                            st.add(int("".join(s)))
                            s[p], s[q] = s[q], s[p]
                    s[i], s[j] = s[j], s[i]
            ans += sum(cnt[v] for v in st)
            cnt[x] += 1
        return ans


s = Solution()
examples = [
    (dict(nums=[1023, 2310, 2130, 213]), 4),
    (dict(nums=[1, 10, 100]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.countPairs(**e))
