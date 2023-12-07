# 460 LFU 缓存


# leetcode submit region begin(Prohibit modification and deletion)
class CacheNode:
    def __init__(self, key=None, value=None, next_=None, prev=None, cnt=0):
        self.key = key
        self.value = value
        self.next = next_
        self.prev = prev
        self.cnt = cnt


class CntNode:
    def __init__(self, cnt=0, next_cnt=None, prev_cnt=None):
        self.cnt = cnt
        self.next = next_cnt
        self.prev = prev_cnt
        self.size = 0
        self.head = CacheNode()
        self.tail = CacheNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __del__(self):
        del self.head
        del self.tail

    def __len__(self):
        return self.size


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cnt_d = dict()
        cnt_1 = CntNode(cnt=1)
        self.cnt_d[1] = cnt_1
        self.cache_d = dict()
        self.size = 0
        self.min_cnt = 1

    def get(self, key: int) -> int:
        if key not in self.cache_d:
            return -1
        node = self.cache_d[key]
        self.update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache_d:
            node = self.cache_d[key]
            node.value = value
            self.update(node)
            return
        if self.size == self.capacity:
            node = self.cnt_d[self.min_cnt].tail.prev
            self.remove(node)
            del self.cache_d[node.key]
            del node
            self.size -= 1
        node = CacheNode(cnt=1, key=key, value=value)
        self.cache_d[key] = node
        self.insert(self.cnt_d[1].head, node)
        self.min_cnt = 1
        self.size += 1

    def update(self, node):
        curr_c = node.cnt
        curr_cnt_node = self.cnt_d[curr_c]
        new_c = curr_c + 1
        self.remove(node)
        node.cnt = new_c
        if new_c in self.cnt_d:
            self.insert(self.cnt_d[new_c].head, node)
        else:
            new_cnt_node = CntNode(cnt=new_c)
            self.cnt_d[new_c] = new_cnt_node
            self.insert(new_cnt_node.head, node)
        # 更新 min_cnt
        if curr_cnt_node.size == 0:
            self.min_cnt = 1
            while True:
                if self.min_cnt in self.cnt_d:
                    if self.cnt_d[self.min_cnt].size != 0:
                        break
                    self.min_cnt += 1

    def insert(self, prev, node):
        # prev 要插入位置的前一个节点
        # node 要插入的节点
        q = prev.next
        node.prev = prev
        node.next = q
        prev.next = node
        q.prev = node
        self.cnt_d[node.cnt].size += 1

    def remove(self, node):
        # node 要删除的节点
        # 仅仅将 node 从原来的位置移开，不 del
        p = node.prev
        q = node.next
        p.next = q
        q.prev = p
        self.cnt_d[node.cnt].size -= 1

    def show(self):
        for k, v in self.cnt_d.items():
            print("cnt=", k)
            p = v.head.next
            while p != v.tail:
                print(p.key, p.value)
                p = p.next
        print("========")


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
obj = LFUCache(2)
# method = ["put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
# args = [[1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
args = [[1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
null = None
answer = [null, null, 1, null, -1, 3, null, -1, 3, 4]
for m, arg, ans in zip(method, args, answer):
    # print(eval(f"obj.{m}()"))
    r = getattr(obj, m)(*arg)
    print(m, arg, ans, r)
    obj.show()
    print()
    # break
# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。 
# 
#  实现 LFUCache 类： 
# 
#  
#  LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象 
#  int get(int key) - 如果键 key 存在于缓存中，则获取键的值，否则返回 -1 。 
#  void put(int key, int value) - 如果键 key 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量 
# capacity 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近最久未使用 的键。 
#  
# 
#  为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。 
# 
#  当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。 
# 
#  函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", 
# "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# 输出：
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
# 
# 解释：
# // cnt(x) = 键 x 的使用计数
# // cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // 返回 1
#                  // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
#                  // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // 返回 -1（未找到）
# lfu.get(3);      // 返回 3
#                  // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
#                  // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // 返回 -1（未找到）
# lfu.get(3);      // 返回 3
#                  // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // 返回 4
#                  // cache=[3,4], cnt(4)=2, cnt(3)=3 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= capacity <= 10⁴ 
#  0 <= key <= 10⁵ 
#  0 <= value <= 10⁹ 
#  最多调用 2 * 10⁵ 次 get 和 put 方法 
#  
# 
#  Related Topics 设计 哈希表 链表 双向链表 👍 717 👎 0
