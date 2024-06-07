class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        # print('init ')

    def set(self, key: str, value: str, timestamp: int) -> None:
        # print('set : [', key,value,timestamp,']')
        self.dic[key].append( (value,timestamp) )

    def get(self, key: str, timestamp: int) -> str:
        # print('get : ', self.dic[key], 'timestamp:',timestamp)
        temp = ""
        n = len(self.dic[key])
        for i in range(n-1, -1, -1):
            # print('  loop: ', self.dic[key][i])
            if timestamp>=self.dic[key][i][1]:
                return self.dic[key][i][0]
        # print()
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)