class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key 
            self.value = value
            self.next = None
            self.tail = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.usage = 0
        self.d = {} # format : { key:Node(val) }
        self.head = self.Node(-11,-11)
        self.tail = self.Node(-99,-99)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        self.deleteNode(node)
        self.addToBack(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.value = value
            self.deleteNode(node)
            self.addToBack(node)
        else:
            if len(self.d) == self.cap:
                # Remove the least recently used (LRU) node
                rmnode = self.head.next
                self.deleteNode(rmnode)
                del self.d[rmnode.key]
            # Add the new node
            newNode = self.Node(key, value)
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

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)