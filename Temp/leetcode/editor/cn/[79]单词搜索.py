# 79 单词搜索
# https://leetcode.cn/problems/word-search/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 特判
        if word == '':
            return True
        c = Counter([x for row in board for x in row])
        cc = Counter(word)
        for key in cc:
            if cc[key] > c[key]:
                return False

        def dfs(i: int, j: int) -> bool:
            if len(path) == len(word):
                return "".join(path) == word
            for di, dj in [(1, 0), (-1, 0), (0, 1,), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in vis:
                    c = board[ni][nj]
                    if c == word[len(path)]:
                        vis.add((ni, nj))
                        path.append(c)
                        if dfs(ni, nj):
                            return True
                        path.pop()
                        vis.remove((ni, nj))
            return False

        vis = set()
        path = []
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                c = board[i][j]
                if c == word[0]:
                    vis.add((i, j))
                    path.append(c)
                    if dfs(i, j):
                        return True
                    path.pop()
                    vis.remove((i, j))
        return False
# leetcode submit region end(Prohibit modification and deletion)
