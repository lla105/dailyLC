class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        maxfreq = 0
        for t in tasks:
            d[t] = d.get(t,0) + 1
            maxfreq = max(maxfreq, d[t])
        # print(d)
        count = 0
        for i,v in d.items():
            if v==maxfreq:
                count += 1
        # print( ' count ; ', count)
        temp = (maxfreq-1) * (n+1)
        temp = temp + count

        if temp > len(tasks):
            return temp
        else:
            return len(tasks)
        