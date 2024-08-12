# 676 实现一个魔法字典
# https://leetcode.cn/problems/implement-magic-dictionary/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# 官解
class MagicDictionary:

    def __init__(self):
        self.words = list()

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue

            diff = 0
            for chx, chy in zip(word, searchWord):
                if chx != chy:
                    diff += 1
                    if diff > 1:
                        break

            if diff == 1:
                return True

        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# leetcode submit region end(Prohibit modification and deletion)
