class TimeMap:

    def __init__(self):
        self.d = defaultdict(list) # format : { 'foo' : [(val, time) , (val2, time2)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append( (value, timestamp) )

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            print( ' get() : key not in d')
            return ""
        arr = self.d[key]
        for i in range(len(arr)-1, -1, -1):
            if arr[i][1] <= timestamp:
                return arr[i][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)