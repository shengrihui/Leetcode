# 47 全排列 II
from itertools import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums)))
# leetcode submit region end(Prohibit modification and deletion)
