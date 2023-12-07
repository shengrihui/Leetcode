# 2251 花期内花的数目
import bisect
from collections import *
from itertools import *
from typing import *


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n = max(max(people), max(e for _, e in flowers))
        diff = [0] * (n + 5)
        for s, e in flowers:
            diff[s] += 1
            diff[e + 1] -= 1
        a = list((accumulate(diff)))
        return [a[i] for i in people]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        cnt = defaultdict(int)
        for s, e in flowers:
            cnt[s] += 1
            cnt[e + 1] -= 1
        a = sorted(cnt.items(), key=lambda x: x[0])
        indies = [i for i, _ in a]
        pre = [0] + list(accumulate([x for _, x in a])) + [0]
        return [pre[bisect.bisect_right(indies, p)] for p in people]

# leetcode submit region end(Prohibit modification and deletion)
