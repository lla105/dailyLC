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

        self.result = set()
        # curList = ['#'] * len(digits) # ['a' , 'd']

        def bf(curList, index):
            if len(curList) == len(digits):
                self.result.add(''.join(curList))
                return
            number = digits[index]
            letters = dic[number]
            for i in range(len(letters)):
                char = letters[i]
                bf(curList + [char] , index+1)
        bf([], 0)
        print(self.result)

        return self.result