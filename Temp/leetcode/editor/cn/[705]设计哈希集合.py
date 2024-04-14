# 705 设计哈希集合
# https://leetcode.cn/problems/design-hashset/


# leetcode submit region begin(Prohibit modification and deletion)
class MyHashSet:

    def __init__(self):
        self.buckets = 1000
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def add(self, key: int) -> None:
        h = self.hash(key)
        if not (key in self.table[h]):
            self.table[h].append(key)

    def remove(self, key: int) -> None:
        h = self.hash(key)
        if key in self.table[h]:
            self.table[h].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.table[self.hash(key)]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# leetcode submit region end(Prohibit modification and deletion)
