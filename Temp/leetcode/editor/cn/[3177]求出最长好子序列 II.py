# 3177 求出最长好子序列 II
# https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-ii/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
"""
f[x][j] 表示以 x 结尾的至多 j 个不相邻的最长好子序列的长度

遍历到 x = nums[i]
1. 不选，f[x][j] 不变
2. 选，接到 x 结尾后面，f[x][j] = f[x][j] + 1
3. 选，接到 y != x 结尾后面，f[x][y] = f[y][j-1] + 1

其中，
1 不需要考虑，因为肯定 选 更优
2 和 3 可以合并，也就是不用判断 y 是否等于 x 直接 f[x][j] = f[y][j-1] + 1 ,因为
再两种都考虑的情况下， f[x][j] = max(f[x][j] + 1, f[x][j-1] + 1) ，而 f[x][j]] >= f[x][j-1] ，因为 
j 越大，越“宽泛”，越能多选~

于是，
f[x][j] = max(f[x][j] + 1, max(f[y][j-1] for y in set) + 1)
其中，因为 nums[i] 的范围大，所以采用 f={} 的方式，set 是已经有的数的集合


但是，还需要枚举 y ，复杂度高
优化：
用 mx 维护 f[·][j] 的最大值
mx = [0] * (k+1)
f[x][j] = max(f[x][j] + 1, mx[j-1] + 1)
mx[j] = max(f[x][j], mx[j])
在求 j 的时候，需要用到 j-1 所以 j 要从大到小

为了减少 if j 的判断，
将 mx 初始化为 k+2 长
下标全部右移一个（python里不用了）

"""


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        fs = {x: [0] * (k + 1) for x in nums}
        mx = [0] * (k + 2)
        for x in nums:
            f = fs[x]
            for j in range(k, -1, -1):
                f[j] = (f[j] if f[j] > mx[j] else mx[j]) + 1
                mx[j + 1] = f[j] if f[j] > mx[j + 1] else mx[j + 1]
        return mx[-1]
# leetcode submit region end(Prohibit modification and deletion)
