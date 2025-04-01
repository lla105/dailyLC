class Solution:
    def isPalindrome(self, s: str) -> bool:
        # eg  s = 'acbca'
        # eg2 s = 'abba'
        nums = '1234567890'
        upper = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
        new_string = ""
        for char in s:
            if char in upper:
                new_string += char.lower()
            elif char in nums:
                new_string += char.lower()
        print(new_string)
        l = len(new_string) - 1
        r = 0
        while r<l:
            if new_string[r] == new_string[l] :
                r += 1
                l -= 1
            else:
                return False

        return True