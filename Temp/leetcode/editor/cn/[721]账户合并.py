# 721 账户合并
# https://leetcode.cn/problems/accounts-merge/
from imports import *

# 并查集1
"""
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_name = dict()  # 邮箱对应的名称
        p = dict()
        vis = dict()  # 记录答案的时候用
        for item in accounts:
            name = item[0]
            for email in item[1:]:
                email_name[email] = name
                p[email] = email
                vis[email] = False

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        # 构造并查集
        for item in accounts:
            for i in range(2, len(item)):
                x, y = item[i], item[i - 1]
                px, py = find(x), find(y)
                if px != py:
                    p[py] = px

        ans = []
        while not all(vis.values()):  # 所有邮箱都访问过
            root = None  # 找到某一个集合的根节点
            for email in p:
                if not vis[email]:
                    root = find(email)
                    break
            name = email_name[root]
            tmp = []
            for email in p:
                # 有相同的该节点（同一个 name ）且没有访问过
                if find(email) == root and not vis[email]:
                    tmp.append(email)
                    vis[email] = True
            ans.append([name] + sorted(tmp))
        return ans
"""


# 并查集2
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_name = dict()  # 邮箱对应的名称
        p = dict()
        for item in accounts:
            name = item[0]
            for email in item[1:]:
                email_name[email] = name
                p[email] = email

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        # 构造并查集
        for item in accounts:
            for i in range(2, len(item)):
                x, y = item[i], item[i - 1]
                px, py = find(x), find(y)
                if px != py:
                    p[py] = px

        t = defaultdict(list)
        for email in email_name:
            t[find(email)].append(email)
        return [[email_name[k]] + sorted(v) for k, v in t.items()]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_indies = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_indies[email].append(i)

        def dfs(i: int) -> None:
            for email in accounts[i][1:]:
                email_set.add(email)
                for j in email_indies[email]:
                    if not vis[j]:
                        vis[j] = True
                        dfs(j)

        vis = [False] * len(accounts)
        ans = []
        for i, account in enumerate(accounts):
            if vis[i]:
                continue
            vis[i] = True
            name = account[0]
            email_set = set()
            dfs(i)
            ans.append([name] + sorted(email_set))
        return ans


# leetcode submit region end(Prohibit modification and deletion)
"""
[["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
"""
