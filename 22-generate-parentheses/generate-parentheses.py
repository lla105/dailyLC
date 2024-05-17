

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # d = { ')':'(', ']':'[' , '}':'{' }
        # open >= closed
        # n >= open
        stack = []
        result = []
        def trav(open,closed):
            if open==n and closed==n:
                result.append(''.join(stack))
                print('1', stack)
                # stack.pop()
                return
            if open<n and closed<n:
                stack.append('(')
                print('2', stack)
                trav(open+1, closed)
                stack.pop()

            if open<=n and closed<open:
                stack.append(')')
                print('3', stack)
                trav(open,closed+1)
                stack.pop()
                
        trav(0,0)
        return result
