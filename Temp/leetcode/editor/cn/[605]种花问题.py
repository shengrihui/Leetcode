# 605 种花问题
from itertools import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        print(([-2] if flowerbed[0] != 1 else []) +
              [i for i, x in enumerate(flowerbed) if x == 1] +
              ([1 + len(flowerbed)] if flowerbed[-1] != 1 else []))
        print([(y - x - 2) // 2 if y - x > 1 else n + 1 for x, y in pairwise(
            ([-2] if flowerbed[0] != 1 else []) + [i for i, x in enumerate(flowerbed) if x == 1] + (
                [1 + len(flowerbed)] if flowerbed[-1] != 1 else []))])
        return n <= sum([(y - x - 2) // 2 if y - x > 1 else n + 1 for x, y in pairwise(
            ([-2] if flowerbed[0] != 1 else []) + [i for i, x in enumerate(flowerbed) if x == 1] + (
                [1 + len(flowerbed)] if flowerbed[-1] != 1 else []))])
# leetcode submit region end(Prohibit modification and deletion)
