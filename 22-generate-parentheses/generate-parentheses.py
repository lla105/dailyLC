class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n==1:
            return ["()"]

        stack = []
        result = [] #an arr that keeps track of all combination of ()()()
        def tt( openb, closeb ) :
            #base case
            if openb==n and closeb==n:
                result.append(''.join(stack))
                # print(f' RESUT += {result}')
                return 
            # add (
            if openb<n:
                stack.append("(")
                # print(f'b >>> {stack}')
                tt(openb+1, closeb)
                stack.pop()
            # add )

            if openb>closeb:
                stack.append(")")
                # print(f'c >>> {stack}')

                tt(openb, closeb+1)
                stack.pop()

        tt(0,0)
        return result

        