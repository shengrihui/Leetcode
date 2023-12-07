# 347 前 K 个高频元素
from collections import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [i[0] for i in sorted(Counter(nums).items(), key=lambda x: -x[1])[:k]]
        return [i for i, _ in Counter(nums).most_common(k)]

# leetcode submit region end(Prohibit modification and deletion)
