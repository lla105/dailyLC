class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        word = []
        for i in range(length):
            char = s[i]
            if char.isalpha() or char.isdigit():
                word.append(char.lower())
        word = ''.join(word)
        print(f'{word}')

        for i in range(len(word)):

            # print(f'{i} : {word[i]} vs {word[-i-1]}')

            if word[i]!=word[-i-1]:
                return False

        return True