class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
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
        output = []
        def bf( curList , dindex ) :
            if len(curList)==len(digits):
                output.append( ''.join(curList) )
                return
            if dindex >= len(digits):
                return
            curnum = digits[dindex]
            letters = self.d[curnum]
            for char in letters :
                for i in range( dindex , len(digits)):
                    bf( curList+[char] , i+1 )
            

        bf( [] , 0 ) 
        return output