class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxfreq = 0
        maxchar = ''
        samemax = 0
        counter = Counter(tasks)
        for i,v in counter.items():
            if v > maxfreq:
                maxfreq = v
                maxchar = i
        for i,v in counter.items():
            if v == maxfreq:
                samemax+=1
        samemax -= 1
        print(maxchar, maxfreq)
        print(samemax)

        temp = (n+1) * (maxfreq-1) + 1 + samemax

        result = 99
        return max(temp, len(tasks))