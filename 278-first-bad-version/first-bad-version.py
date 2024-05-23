# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=0
        r=n
        while l<=r:
            m = (l+r) // 2
            curr = isBadVersion(m)
            if isBadVersion(m-1) is False and curr is True:
                return m
            if curr is True:
                r = m - 1
            else:
                l = m + 1