class LRUCache:
    class ListNode:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.usage = 0
        self.head = self.ListNode(-11,-11)
        self.tail = self.ListNode(-99,-99)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = {} # format = { key:ListNode()}

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        self.deleteNode(node)
        self.addToBack(node)
        return node.val

    def put(self, key: int, val: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = val
            self.deleteNode(node)
            self.addToBack(node)
        else:
            if len(self.d) == self.cap:
                # Remove the least recently used (LRU) node
                rmnode = self.head.next
                self.deleteNode(rmnode)
                del self.d[rmnode.key]
            # Add the new node
            newNode = self.ListNode(key, val)
            self.d[key] = newNode
            self.addToBack(newNode)
    def addToBack(self, node):
        node.next = self.tail
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
# EG1:
# 1,2,3, cap = 3
# 1,2,3,4
# H,1,3,4,2,T
# put(1,11), put(2,22), put(3,33)
# d1 = {1:11 , 2:22, ...}
# d1 = format = { key:NodeList(key, value)}
# 1,3,4,2,5,T

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)