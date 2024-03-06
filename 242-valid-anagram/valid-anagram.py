class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        ss = sorted(s)
        tt = sorted(t)

        if ss!=tt:
            return False
        else:
            return True