class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        bracketpairs = []

        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            if s[i]==')':
                prevopen = stack.pop()
                bracketpairs.append( (prevopen, i))
        print(stack)
        print(bracketpairs)
        slist = list(s)
        print(slist)
        for i,j in bracketpairs:
            while i<j:
                slist[i],slist[j] = slist[j],slist[i]
                i+=1
                j-=1

        result = ''
        for char in slist:
            if char!='(' and char!=')':
                result += char
        return ''.join(result)