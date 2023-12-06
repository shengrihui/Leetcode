# 2559 统计范围内的元音字符串数
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        pre = list(map(int, [w[0] in "aeiou" and w[-1] in "aeiou" for w in words]))
        for i in range(1, n):
            pre[i] += pre[i - 1]
        ans = []
        for l, r in queries:
            ans.append(pre[r] - (pre[l - 1] if l > 0 else 0))
            # ans.append(sum(pre[l:r + 1]))
        return ans
# leetcode submit region end(Prohibit modification and deletion)


# 给你一个下标从 0 开始的字符串数组 words 以及一个二维整数数组 queries 。 
# 
#  每个查询 queries[i] = [li, ri] 会要求我们统计在 words 中下标在 li 到 ri 范围内（包含 这两个值）并且以元音开头和结尾
# 的字符串的数目。 
# 
#  返回一个整数数组，其中数组的第 i 个元素对应第 i 个查询的答案。 
# 
#  注意：元音字母是 'a'、'e'、'i'、'o' 和 'u' 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
# 输出：[2,3,0]
# 解释：以元音开头和结尾的字符串是 "aba"、"ece"、"aa" 和 "e" 。
# 查询 [0,2] 结果为 2（字符串 "aba" 和 "ece"）。
# 查询 [1,4] 结果为 3（字符串 "ece"、"aa"、"e"）。
# 查询 [1,1] 结果为 0 。
# 返回结果 [2,3,0] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
# 输出：[3,2,1]
# 解释：每个字符串都满足这一条件，所以返回 [3,2,1] 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 10⁵ 
#  1 <= words[i].length <= 40 
#  words[i] 仅由小写英文字母组成 
#  sum(words[i].length) <= 3 * 10⁵ 
#  1 <= queries.length <= 10⁵ 
#  0 <= queries[j][0] <= queries[j][1] < words.length 
#  
# 
#  Related Topics 数组 字符串 前缀和 👍 69 👎 0
