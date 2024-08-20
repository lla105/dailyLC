class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mostfreq = 0
        d2 = defaultdict(list) # format : { freq:[char1, char2] }
        d = defaultdict(list)
        for i in range(len(tasks)):
            t = tasks[i]
            d[t] = d.get(t,0) + 1
            mostfreq = max(mostfreq, d[t])
        print(d, mostfreq)
        mostfreqchars = []
        for i,v in d.items():
            if mostfreq == v:
                mostfreqchars.append(i)
        print(' mots freq chars : ', mostfreqchars)

        temp = mostfreq - 1
        temp2 = n+1
        temp = temp * temp2
        temp += len(mostfreqchars)
        if temp < len(tasks):
            return len(tasks)
        else:
            return temp
        # (most freq -1) * (n+1) ) + rest 

        # a a c a
        # n = 1
        # a c a i a
        # n = 2
        # a c i a i i a

        # a a a c 
        # n = 1
        # a c a c
        # n = 2
        # a c a c
        # n = 4
        # a c i a c
        # a c i i i a i i i i a 

        # n = 3
        # aciiaiiia