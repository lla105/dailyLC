class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.recentq = deque()
        self.capacity = capacity 
        self.usage = 0

    def get(self, key: int) -> int:
        if key in self.d :
            self.recentq.remove(key)
            self.recentq.append(key)
            return self.d[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.recentq.remove(key)
            self.recentq.append(key)
            self.d[key] = value
        else:
            self.usage += 1
            if self.usage > self.capacity:
                temp = self.recentq.popleft()
                self.d.pop(temp)
                self.usage -= 1
            self.recentq.append(key)
            self.d[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)