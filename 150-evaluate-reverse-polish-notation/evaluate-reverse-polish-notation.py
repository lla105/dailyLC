class Solution:
    def operations(self, prefix, operation, postfix):
        if operation=="+":
            return prefix+postfix
        elif operation=="-":
            return prefix-postfix
        elif operation =="*":
            return prefix*postfix
        else:
            return int(prefix/postfix)


    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        # def operation(prefix, )
        stack = []
        for t in tokens:
            if t in operators:
                postfix = stack.pop()
                prefix = stack.pop()
                result = int(self.operations(prefix, t, postfix))
                stack.append(result)
            else:
                # is a number:
                stack.append( int(t) )
        return stack[0]