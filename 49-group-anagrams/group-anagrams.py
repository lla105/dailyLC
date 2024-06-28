class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} # format : { key:[value1,value2] }

        for i in range(len(strs)):
            ss = sorted(strs[i])
            # print(ss)
            ss = ''.join(ss)
            if ss in d:
                d[ss].append(strs[i])
            else:
                d[ss] = [ strs[i] ]

        result = []
        for i,v in d.items():
            result.append(v)
        return result