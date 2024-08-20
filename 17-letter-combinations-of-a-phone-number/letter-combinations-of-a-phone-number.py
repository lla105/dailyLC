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
        self.result = []
        def bf(curList , index):
            if len(curList) == len(digits) and curList:
                self.result.append( ''.join(curList) )
            for i in range(index , len(digits)):
                digit = digits[i]
                if digit in self.d:
                    chars = self.d[digit]
                    for char in chars:
                        bf( curList+[char] , i+1)

        bf([], 0)
        return self.result
        # for digit in digits:
        #     if digit in self.d:
        #         chars = self.d[digit]
        #         for char in chars:
