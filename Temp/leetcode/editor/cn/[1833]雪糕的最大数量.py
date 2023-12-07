# 1833 雪糕的最大数量
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # costs.sort()
        # for i, c in enumerate(costs):
        #     if coins >= c:
        #         coins -= c
        #     else:
        #         return i
        # return len(costs)
        arr = [0] * (max(costs) + 1)
        for c in costs:
            arr[c] += 1
        ans = 0
        for cost, cnt in enumerate(arr):
            for i in range(cnt):
                if coins >= cost:
                    coins -= cost
                    ans += 1
                else:
                    return ans
        return ans
# leetcode submit region end(Prohibit modification and deletion)
