class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # w1 = yyyeytion
        # w2 = execution
        # word1 = 'abd'
        # word2 = 'acd'
        w1 = word1
        w2 = word2
        cache = []
        count = len(w2)
        for i in range(len(w2)+1):
            if i == len(w2):
                temp = []
                for j in range(len(w1), -1, -1):
                    temp.append(j)
            else:
                temp = [ float('inf') ] * (len(w1)+1)
                temp[-1] = count
                count -= 1
            cache.append(temp)
        print(len(cache), ' vs ', len(cache[0]))
        for row in cache:
            print(row)

        # word1 = 'abd' 
        # word2 = 'acd'
        def trav(i,j):
            if j==len(w1) or i==len(w2):
                return cache[i][j]
            if type(cache[i][j]) != float :
                return cache[i][j]
            inst = trav(i+1 , j)
            delete = trav(i,j+1)
            replace = trav(i+1,j+1)
            if w1[j]==w2[i] :
                # cache[i][j] = min(inst, delete, replace)
                cache[i][j] = trav(i+1, j+1)
            else:
                cache[i][j] = min(inst, delete, replace) + 1
            return cache[i][j]
        return trav(0,0)

        return 99