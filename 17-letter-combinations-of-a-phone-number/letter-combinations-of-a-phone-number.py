class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits :
            return result
        
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
        def backtrack(index, curCombination):
            if len(curCombination) == len(digits):
                result.append(curCombination[:])
                return
            
            # for i in range(len(digits[index])):
            #     letter = dic[digits[index]]
            # for letter in dic[digits[index]]:
            for letter in dic[digits[index]]:
                nextIndex = index+1
                tempCombo = curCombination + letter
                backtrack(nextIndex , tempCombo)
                # backtrack(index + 1, curCombination + letter)
        backtrack(0,"")
        return result