# 1333 餐厅过滤器
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> \
    List[int]:
        return [i for i, r in sorted([(id_, r) for id_, r, v, p, d in restaurants if
                                      (not veganFriendly or v) and p <= maxPrice and d <= maxDistance],
                                     key=lambda x: (-x[1], -x[0]))]
# leetcode submit region end(Prohibit modification and deletion)
