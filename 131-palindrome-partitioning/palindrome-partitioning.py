class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = set()

        def bf(curList, startindex):
            if startindex >= len(s):
                result.add( tuple(curList) )
                return
            for i in range(startindex, len(s)):
                string1 = s[startindex:i+1]
                string2 = ''.join(reversed(s[startindex:i+1]))
                if string1 == string2:
                    bf(curList + [string1] , i+1)

        bf([] , 0)
        return result