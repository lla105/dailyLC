class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def printlist(somelist):
            print('print() : ', end=' ')
            for num in somelist:
                print(num,end='')
            print()
        if y > x:
            xy = y
            dominant = 'ba'
            nondom = 'ab'
        else:
            xy = x
            dominant = 'ab'
            nondom = 'ba'
        print('s       : ', s, 'dom:',dominant,'nondom:',nondom)
        
        domcount = 0
        nondomcount = 0

        stack = []
        printlist(stack)
        print()

        for i in range(len(s)):
            if stack and s[i]==dominant[1]:
                if stack[-1]==dominant[0]:
                    domcount+=1
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        print(s)
        print(''.join(stack))
        news = ''.join(stack)
        stack = []
        for i in range(len(news)):
            if stack and news[i]==nondom[1]:
                if stack[-1]==nondom[0]:
                    nondomcount+=1
                    stack.pop()
                else:
                    stack.append(news[i])
            else:
                stack.append(news[i])
        printlist(stack)
        answer = ( max(x,y)*domcount ) + ( min(x,y)*nondomcount )
        return answer