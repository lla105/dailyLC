class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for word in strs:
            sorted_word = sorted(word)
            # print(word, " ... ", sorted_word)
            sorted_word = ''.join(sorted_word)
            # print(sorted_word)
            if (sorted_word not in d):
                d[sorted_word] = [word]
            else:
                d[sorted_word].append(word)

        # print(d.values())
        return d.values()