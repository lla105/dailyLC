class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 1 or n == 2: 
            return True
        if n==0:
            return False
        if n % 2 != 0:
            print( n%2 , ' ??')
            return False
        if n< 0 :
            return False
        num = 2
        while num < n :
            num = num * 2
            # print('num: ', num)
            if num == n :
                return True
            if num > n :
                return False
        return False