class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        # tempset = {' ', ',', '.', ':', ';', '@', '#'}
        news = s
        s = ''
        for i in range(len(news)):
            # if news[i] not in tempset:
            if news[i].isalpha() or news[i].isdigit():
                s += news[i].lower()
        right = len(s)-1

        print(s)
        while left<right:
            print(s[left].lower(), s[right].lower())
            if s[left].lower() != s[right].lower() :
                # print(s[left].lower(), s[right].lower())
                return False
            left+=1
            right -=1
        return True