class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(s1)):
            d1[s1[i]] = d1.get(s1[i], 0) + 1
            d2[s2[i]] = d2.get(s2[i], 0) + 1
        if d1==d2:
            return True
        print(d1,d2)
        for i in range(len(s1), len(s2)):
            leftindex = i-len(s1)
            rightindex = i
            d2[ s2[leftindex] ] -= 1
            if d2[s2[leftindex]]<=0:
                d2.pop( s2[leftindex] )
            d2[ s2[rightindex] ] = d2.get( s2[rightindex] , 0 ) + 1
            if d1==d2:
                return True
        return False