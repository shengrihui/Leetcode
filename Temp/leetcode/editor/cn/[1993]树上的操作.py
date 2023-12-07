# 1993 树上的操作
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.n = n
        self.parent = parent
        self.status = [False] * n
        self.lock_user = [0] * n
        self.son = [[] for _ in range(n)]
        for i, p in enumerate(parent):
            if i == 0:
                continue
            self.son[p].append(i)
        self.flag = False

    def lock(self, num: int, user: int) -> bool:
        if not self.status[num]:
            self.status[num] = True
            self.lock_user[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.status[num] and self.lock_user[num] == user:
            self.status[num] = False
            self.lock_user[num] = user
            return True
        return False

    def dfs(self, num):
        # 对num节点解锁，self.flag标记有没有操作了
        self.flag |= self.status[num]
        self.status[num] = False  # 给num解锁
        self.lock_user[num] = 0
        if not self.son[num]:
            return
        for s in self.son[num]:
            self.dfs(s)

    def upgrade(self, num: int, user: int) -> bool:
        # 条件一，指定节点当前状态为未上锁。
        if self.status[num]:
            return False
        # 条件三，指定节点没有任何上锁的祖先节点。
        # 条件二在判断的时候就可以直接操作了，但前提是条件三也满足
        p = self.parent[num]
        while p != -1:
            if self.status[p]:
                return False
            p = self.parent[p]
        # 条件二，指定节点至少有一个上锁状态的子孙节点（可以是 任意 用户上锁的）。
        self.flag = False
        self.dfs(num)
        if not self.flag:
            return False
        # 操作
        self.status[num] = True
        self.lock_user[num] = user
        return True

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
# leetcode submit region end(Prohibit modification and deletion)
