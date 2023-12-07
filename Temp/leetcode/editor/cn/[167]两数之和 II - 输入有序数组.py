# 167 两数之和 II - 输入有序数组
from typing import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while True:
            m = numbers[i] + numbers[j]
            if m > target:
                j -= 1
            elif m < target:
                i += 1
            else:
                return [i + 1, j + 1]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(numbers):
            if target - x in d:
                return [d[target - x], i + 1]
            d[x] = i + 1
# leetcode submit region end(Prohibit modification and deletion)
