# 146 LRU 缓存
from typing import *
from collections import *
from itertools import *
from functools import *


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

# 
#  请你设计并实现一个满足 
#  LRU (最近最少使用) 缓存 约束的数据结构。
#  
# 
#  
#  实现 
#  LRUCache 类：
#  
# 
#  
#  
#  
#  LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存 
#  int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。 
#  void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 
# key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。 
#  
#  
#  
# 
#  函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。 
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 10000 
#  0 <= value <= 10⁵ 
#  最多调用 2 * 10⁵ 次 get 和 put 
#  
# 
#  Related Topics 设计 哈希表 链表 双向链表 👍 2880 👎 0
