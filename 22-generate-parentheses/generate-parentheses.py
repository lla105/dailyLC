class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        resultlist = []

        def trav(open, close):
            if open==n and close==open:
                print('1:', stack)
                resultlist.append(''.join(stack))
                return 
            if open<n and close<n:
                stack.append('(')
                print('2:', stack)
                trav(open+1, close)
                stack.pop()
            if close<open and open<=n and stack[-1]:
                stack.append(')')
                print('3:', stack)
                trav(open,close+1)
                stack.pop()
            
        
        trav(0,0)
        return resultlist