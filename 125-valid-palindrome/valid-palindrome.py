class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        print(f'length : {length}')
        ss = []
        for i in range(length):
            if s[i].isalpha() or s[i].isdigit():
                ss.append(s[i].lower())
        ss = ''.join(ss)
        print(f'ss : {ss}')
        # s = ss
        # print(f's  : {s}')

        for i in range(len(ss)):
            # if s[i].lower() != s[-1].lower():
            print(f'{ss[i]} vs {ss[-i]}')
            if ss[i] != ss[-i-1]:
                return False

        return True