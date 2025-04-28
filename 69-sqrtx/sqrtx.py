class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        if x==2:
            return 1
        num = 2
        prev = 2
        for i in range( 2, x ):
            if i*i > x:
                return i-1
        return prev