class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] # to keep track of each combination
        result = [] #colletion of combinations of brackets

        def backtrack(openbs, closebs) :
            #a)
            if openbs==closebs and closebs==n: 
                print(f'appending stack: {stack}')
                result.append(''.join(stack))
                # stack=[]
                return
            #b)
            if openbs<n:
                # can only have open bs next
                stack.append("(")
                backtrack(openbs+1, closebs)
                stack.pop()
            #c)
            if openbs>closebs:
                # next can be open or close
                stack.append(")")
                backtrack(openbs, closebs+1) 
                stack.pop()
            


        backtrack(0,0)
        return result