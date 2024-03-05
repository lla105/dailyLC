class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) :
            return False
        ss = sorted(s)
        st = sorted(t)
        if ss==st:
            return True
                