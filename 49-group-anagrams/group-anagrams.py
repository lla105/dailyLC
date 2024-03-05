class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = defaultdict(list)

        for word in strs:
            sorted_key = sorted(word)
            sorted_key = ''.join(sorted_key)
            # print(sorted_key)
            dict[sorted_key].append(word)

        print(list(dict.values()))
        return list(dict.values())
        # print(list(dict.values()))