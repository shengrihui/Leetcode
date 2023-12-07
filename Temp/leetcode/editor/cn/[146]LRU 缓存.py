# 146 LRU 缓存


# leetcode submit region begin(Prohibit modification and deletion)
class CacheNode:
    def __init__(self, key=None, value=None, next_=None, prior=None):
        self.key = key
        self.value = value
        self.next = next_
        self.prior = prior


class LRUCache:

    def __init__(self, capacity: int):
        self.d = dict()
        self.capacity = capacity
        # 离head近的事最忌用过的
        self.head = CacheNode()
        self.tail = CacheNode()
        self.head.next = self.tail
        self.tail.prior = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        # 将这个移动到head后面
        node = self.d[key]
        p = node.prior
        q = node.next
        p.next = q
        q.prior = p
        node.next = self.head.next
        node.next.prior = node
        self.head.next = node
        node.prior = self.head
        # print("get", key)
        # self.showCache()
        return node.value

    def put(self, key: int, value: int) -> None:
        # print("put", key, value)
        if key in self.d:
            self.d[key].value = value
            t = self.get(key)  # 更新
            # self.showCache()
            return
        if self.size == self.capacity:
            # print("删除")
            # self.showCache()
            # 删掉离为节点最近的
            p = self.tail.prior
            p_key = p.key
            # print("del p key", p_key)
            # self.showCache()
            self.tail.prior = p.prior
            self.tail.prior.next = self.tail
            del p
            del self.d[p_key]
            self.size -= 1
        node = CacheNode(key, value, next_=self.head.next, prior=self.head)
        self.head.next.prior = node
        self.head.next = node
        self.d[key] = node
        self.size += 1
        # self.showCache()
        # print()

    def showCache(self):
        print("正着")
        p = self.head.next
        while p != self.tail:
            print(f"key={p.key} ,v={p.value}")
            p = p.next
        print("反着")
        p = self.tail.prior
        while p != self.head:
            print(f"key={p.key} ,v={p.value}")
            p = p.prior
        # print(self.d)
        print("============")


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
"""
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
"""
