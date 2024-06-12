class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        result = []
        for i in range(len(strs)):
            # print(strs[i])
            # temp = sorted(strs[i])
            # print(temp)
            string = ''.join(sorted(strs[i]))
            # print(string)
            if string in d:
                d[string].append(strs[i])
            else:
                d[string] = [strs[i]]
        for i,v in d.items():
            # print(i,v)
            result.append(v)

        return result