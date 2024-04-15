# 706 设计哈希映射
# https://leetcode.cn/problems/design-hashmap/


# leetcode submit region begin(Prohibit modification and deletion)
class MyHashMap:

    def __init__(self):
        self.buckets = 1000
        self.map = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        h = self.hash(key)
        for i, (k, v) in enumerate(self.map[h]):
            if k == key:
                self.map[h][i] = (key, value)
                return
        self.map[h].append((key, value))

    def get(self, key: int) -> int:
        for k, v in self.map[self.hash(key)]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        for k, v in self.map[h]:
            if k == key:
                self.map[h].remove((k, v))
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# leetcode submit region end(Prohibit modification and deletion)
