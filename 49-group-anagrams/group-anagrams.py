class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = defaultdict(list)
        count = 1
        print( "0) ", anagram_map)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
            # sorted_word = ''.join(sorted(word))
            # print(">>>> ", sorted_word)
            # anagram_map[sorted_word].append(word)
            # print(count, ") ", anagram_map)
            # count +=1

        return list(anagram_map.values())