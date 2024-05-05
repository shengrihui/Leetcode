# 1652 拆炸弹
# https://leetcode.cn/problems/defuse-the-bomb/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        if k > 0:
            i, j = 1, k
            s = sum(code[i:j + 1])
        else:
            i, j = k, -1
            s = sum(code[i:])
        ans = [s]
        for p in range(n - 1):
            j = (j + 1 + n) % n
            s += code[j] - code[i]
            i = (i + 1 + n) % n
            ans.append(s)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
