class Solution:
    # operatorslist = ["+", "*", "/", "-"]
    # def operation(self, prefix, operator, postfix):
    #     if operator=="+":
    #         temp = prefix+postfix
    #         print("temp", temp)
    #         return temp
    #     if operator=="-":
    #         return prefix-postfix
    #     if operator=="*":
    #         print(prefix, "*", postfix)
    #         return prefix*postfix
    #     if operator=="/":
    #         temp = int(prefix/postfix)
    #         # if temp<1:
    #         #     temp = 0
    #         return temp 


    def evalRPN(self, tokens):
        stack = []
        for c in tokens:
            if c =="+":
                stack.append(stack.pop() + stack.pop())
            elif c=="-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                a,b = stack.pop(), stack.pop()
                stack.append(a*b)
            elif c=="/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]
        # s = []
        # for t in tokens:
            
        #     if t not in self.operatorslist:
        #         print("appending : ", t)
        #         s.append(int(t))
        #     else:
        #         print("not number: ", t)
        #         # is an operator 
        #         if len(s)<=1:
        #             return 0
        #         else:
        #             # stack has >2 items
        #             temppostfix = s.pop()
        #             print("post: ", temppostfix)
        #             postfix = int(temppostfix)

        #             tempprefix = s.pop()
        #             print("pre: ", tempprefix)
        #             prefix = int(tempprefix)

        #             print(">>>",prefix,t,postfix)
        #             remain = self.operation(prefix,t,postfix)
        #             print(f"remain: {remain}")

        #             s.append(remain)
        #     print("stack(end): ", s,'\n')
                

        # # answer = 0
        
        # return s[0]
