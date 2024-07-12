class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ''
        ddic = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        result = set()
        def backtrack( curList, index):
            print(curList, index)
            if index>=len(digits):
            # if len(curList) == len(digits):
                result.add( ''.join(curList) )
                return
            curnum = digits[index]
            letters = ddic[curnum]

            for i in range(len(letters)):
                char = letters[i]
                backtrack(curList+[char] , index+1)
        backtrack([] , 0)

        return result
