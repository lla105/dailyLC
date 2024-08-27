class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.d = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        result = []
        if not digits:
            return result
        def bf( curList , index) :
            if len(curList) == len(digits):
                result.append( ''.join(curList) )
            for i in range( index, len(digits)):
                if digits[i] not in self.d:
                    continue
                letters = self.d[digits[i]]
                for char in letters:
                    bf( curList+[char] , i+1 )
        bf( [] , 0)

        return result