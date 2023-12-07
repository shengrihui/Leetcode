# 2661 找出叠涂元素
from functools import *
from itertools import *
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        for ele in map(partial(map, {x: k for k, x in enumerate(arr)}.get), chain(mat, zip(*mat))):
            print(list(ele))
        return min(map(max, map(partial(map, {x: k for k, x in enumerate(arr)}.get), chain(mat, zip(*mat)))))
        # mn, m, n = len(arr), len(mat), len(mat[0])
        # mp = [[0, 0]] * (mn + 1)
        # for i, row in enumerate(mat):
        #     for j, x in enumerate(row):
        #         mp[x] = [i, j]
        # M, N = [n] * m, [m] * n
        # for idx, x in enumerate(arr):
        #     i, j = mp[x]
        #     M[i] -= 1
        #     N[j] -= 1
        #     if M[i] == 0 or N[j] == 0:
        #         return idx

# leetcode submit region end(Prohibit modification and deletion)


# 给你一个下标从 0 开始的整数数组 arr 和一个 m x n 的整数 矩阵 mat 。arr 和 mat 都包含范围 [1，m * n] 内的 所有 整数
# 。 
# 
#  从下标 0 开始遍历 arr 中的每个下标 i ，并将包含整数 arr[i] 的 mat 单元格涂色。 
# 
#  请你找出 arr 中在 mat 的某一行或某一列上都被涂色且下标最小的元素，并返回其下标 i 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：arr = [1,3,4,2], mat = [[1,4],[2,3]]
# 输出：2
# 解释：遍历如上图所示，arr[2] 在矩阵中的第一行或第二列上都被涂色。
#  
# 
#  示例 2： 
#  
#  
# 输入：arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
# 输出：3
# 解释：遍历如上图所示，arr[3] 在矩阵中的第二列上都被涂色。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n = mat[i].length 
#  arr.length == m * n 
#  1 <= m, n <= 10⁵ 
#  1 <= m * n <= 10⁵ 
#  1 <= arr[i], mat[r][c] <= m * n 
#  arr 中的所有整数 互不相同 
#  mat 中的所有整数 互不相同 
#  
# 
#  Related Topics 数组 哈希表 矩阵 👍 25 👎 0
