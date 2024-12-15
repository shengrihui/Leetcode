# 1338 数组大小减半
# https://leetcode.cn/problems/reduce-array-size-to-the-half/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = Counter(arr)
        s = 0
        for i, (x, c) in enumerate(sorted(cnt.items(), key=lambda x: -x[1])):
            s += c
            if s >= n // 2:
                return i + 1


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = sorted(Counter(arr).values(), reverse=True)
        m = len(arr) // 2
        for i, s in enumerate(accumulate(cnt)):
            if s >= m:
                return i + 1

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/reduce-array-size-to-the-half/solutions/3004655/ji-shu-cong-da-dao-xiao-tan-xin-pythonja-9vth/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# leetcode submit region end(Prohibit modification and deletion)
