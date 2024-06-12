class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        print(d)
        max_freq = 0
        max_char = ''
        same_max = 0
        for i,v in d.items():
            if v>max_freq:
                max_freq = v
                max_char = i
        for i,v in d.items():
            if v==max_freq:
                same_max+=1
        if same_max>0:
            same_max -= 1
        print(max_freq, max_char, same_max)
        temp = (n+1) * (max_freq-1)
        temp += 1
        temp += same_max
        return max(temp, len(tasks))
        