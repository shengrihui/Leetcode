# 661 图片平滑器
# https://leetcode.cn/problems/image-smoother/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        ans = [[0] * m for _ in range(n)]
        dirs = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)]
        for i, row in enumerate(img):
            for j, x in enumerate(row):
                s = c = 0
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        s += img[ni][nj]
                        c += 1
                ans[i][j] = s // c
        return ans
# leetcode submit region end(Prohibit modification and deletion)
