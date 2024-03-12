class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def tt(index, path):
            #base case
            if index == len(digits):
                result.append(''.join(path))
                return
            
            for char in mappings[digits[index]]:
                path.append(char)
                tt(index+1, path)
                path.pop()
            
        result = []
        tt(0,[])
        return result