class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        reversednum = 0
        temp = x

        while temp!=0:
            digit = temp%10
            reversednum = reversednum*10 + digit
            temp = temp//10

        if (reversednum==x):
            return True