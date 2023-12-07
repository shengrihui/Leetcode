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
