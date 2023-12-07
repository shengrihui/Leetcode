# 208 实现 Trie (前缀树)


# leetcode submit region begin(Prohibit modification and deletion)
class Trie:

    def __init__(self):
        self.son = [[-1] * 26]
        self.isEnd = [[False] * 26]
        self.idx = 0

    def insert(self, word: str) -> None:
        p = u = 0
        for c in word:
            u = ord(c) - ord("a")
            if self.son[p][u] == -1:
                self.son.append([-1] * 26)
                self.isEnd.append([False] * 26)
                self.idx += 1
                self.son[p][u] = self.idx
            p = self.son[p][u]
        self.isEnd[p][u] = True

    def search(self, word: str) -> bool:
        p = u = 0
        for c in word:
            u = ord(c) - ord("a")
            if self.son[p][u] == -1:
                return False
            p = self.son[p][u]
        return self.isEnd[p][u]

    def startsWith(self, prefix: str) -> bool:
        p = u = 0
        for c in prefix:
            u = ord(c) - ord("a")
            if self.son[p][u] == -1:
                return False
            p = self.son[p][u]
        return True

    def show(self):
        for i, (s, e) in enumerate(zip(self.son, self.isEnd)):
            print(i)
            print(s)
            print(e)
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)
