class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # build dict for p

        # loop over s 
        # build dict for s[i-len(p): i]
        # compare occurance for each entry  
        # if match, record the index.(i)

        #to move to next subset, remove s[i-len(p)] from dict
        # add next s[i] to dict. repeat. 
        pdic = Counter(p)
        sdic = {}
        result = []
        for i in range( len(s)):
            # print(s[i])
            sdic[s[i]] = sdic.get(s[i],0) + 1
            if i<len(p)-1:
                continue
            # print('1) ', s[i] , '->', sdic)

            isAnagram = True
            for pi, pv in pdic.items():
                if pi in sdic and pv==sdic.get(pi):
                    # print('2)   match: ', pi, pv)
                    pass
                else:
                    isAnagram = False
                    continue
            if isAnagram :
                # print('3)    result append : ', i-len(p)+1)
                result.append(i-len(p)+1)
            # print('4)     sdic pop : ', s[i-len(p)+1])
            if sdic.get(s[i-len(p)+1]) == 1:
                sdic.pop(s[i-len(p)+1])
            elif sdic.get(s[i-len(p)+1]) >1:
                sdic[s[i-len(p)+1]] -= 1
        return result
