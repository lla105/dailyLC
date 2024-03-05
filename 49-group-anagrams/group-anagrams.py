class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)

        for word in strs:
            sortedWord = sorted(word)
            sortedWord = ''.join(sortedWord)
            d[sortedWord].append(word)


        print(list(d.values()))
        return list(d.values())