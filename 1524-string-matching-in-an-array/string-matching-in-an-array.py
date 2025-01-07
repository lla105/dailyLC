class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        maxlen = 0
        d = defaultdict(list)
        for i in range(len(words)):
            maxlen = max( maxlen , len(words[i]) )
            d[ len(words[i]) ].append( words[i] )

        # print( d)
        newwords = []
        for i in range(maxlen+1):
            if i not in d:
                continue
            for j in range(len(d[i])):
                newwords.append( d[i][j] )
        # print(newwords)
        output = []
        seen = set()
        for i in range(len(newwords)):
            for j in range(i+1 , len(newwords)):
                print( newwords[i], ' vs ', newwords[j])
                if newwords[i] in newwords[j] and newwords[i] not in seen:
                    seen.add( newwords[i] )
                    output.append( newwords[i] )
        return output