class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                string = strs[j]
                if i==len(string) or string[i] != strs[0][i]:
                    return output
            output += strs[0][i]

        return output