# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        m = (l+r)//2

        while l<=r:
            m = (l+r)//2
            if isBadVersion(m) is True:
                r = m-1
            else:
                if isBadVersion(m+1) is True:
                    return m+1
                else:
                    l = m+1
        return m