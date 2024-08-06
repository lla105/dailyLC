class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word)<=8:
            return len(word)
        d1 = {}
        for i in range(len(word)):
            d1[word[i]] = d1.get(word[i], 0)+1
        print(d1)
        # dicSet = defaultdict(set)
        d2 = defaultdict(list)
        for i,v in d1.items():
            # dicSet[v].add(i)
            d2[v].append(i)
        print(d2)
        # print(' word length : ', len(word)-1)
        numstack = []
        print( ' len ( word ) : ', len(word))
        for i in range( len(word), -1, -1):
            if i not in d2:
                continue
            for numindex in d2[i]:
                numstack.append([numindex])
        print(' num stack: ', numstack)
        presscount = 0
        level = 1
        curlevelcount = 0
        for i in range(len(numstack)):
            # print('. ', d1[numstack[i][-1]],level)
            presscount += level * d1[numstack[i][-1]]
            
            curlevelcount +=1
            print(' >> ', level, ': ', numstack[i][-1],' -> freq : ', d1[numstack[i][-1]])
            if curlevelcount >= 8:
                print( ' >>>>> level count over 7')
                curlevelcount = 0
                level += 1
        return presscount
# 6+12 = 18
