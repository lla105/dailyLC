class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        sdic = {}
        for char in s:
            if char in sdic:
                sdic[char] += 1
            else:
                sdic[char] = 1
        # print(sdic)

        for char in t:
            if char in sdic:
                sdic[char] -= 1
                if sdic[char] <=0:
                    sdic.pop(char)
            else:
                return False

        return True