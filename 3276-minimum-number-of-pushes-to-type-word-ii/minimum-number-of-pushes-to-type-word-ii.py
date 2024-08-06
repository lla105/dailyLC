class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word)<=8:
            return len(word)
        d1 = {}
        for i in range(len(word)):
            d1[word[i]] = d1.get(word[i], 0)+1
        # dicSet = defaultdict(set)
        d2 = defaultdict(list)
        for i,v in d1.items():
            # dicSet[v].add(i)
            d2[v].append(i)
        # print(' word length : ', len(word)-1)
        numstack = []
        for i in range( len(word), -1, -1):
            if i not in d2:
                continue
            for numindex in d2[i]:
                numstack.append([numindex])
        presscount = 0
        level = 1
        curlevelcount = 0
        for i in range(len(numstack)):
            # print('. ', d1[numstack[i][-1]],level)
            presscount += level * d1[numstack[i][-1]]
            
            curlevelcount +=1
            if curlevelcount >= 8:
                curlevelcount = 0
                level += 1
        return presscount
# 6+12 = 18
