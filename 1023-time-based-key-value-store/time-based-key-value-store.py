class TimeMap:

    def __init__(self):
        self.d = defaultdict(list) 
        # format : { key : (value , timestamp) , (value2, timestamp2) }

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append( (value, timestamp) )
        else:
            self.d[key] = [ (value,timestamp) ]
            
    def get(self, key: str, timestamp: int) -> str:
        if key in self.d :
            for i in range(len(self.d[key])-1, -1, -1):
                # print('>>>>', self.d[key][1])
                if self.d[key][i][1] <= timestamp:
                    return self.d[key][i][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)