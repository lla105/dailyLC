class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dic = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        result = []
        def bt(curArray, numIndex):
            if len(curArray) == len(digits):
                result.append(''.join(curArray))   
                return
            letters = dic[digits[numIndex]]
            for letter in letters:
                # curArray.append(letter)

                bt(curArray + [letter] , numIndex+1)
                # curArray.pop()
            return
        bt([] , 0)
        return result
            