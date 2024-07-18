class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def bt(openb, closeb, curlist, level):
            if closeb==openb and openb==n:
                print(level*'  ', 'APPEND')
                result.append(''.join(curlist))
                return
            if n>openb and n>closeb:
                print(level*'  ','ADDING OPEN')
                bt(openb+1, closeb, curlist+['('], level+1)
            if openb<=n and openb>closeb:
                print(level*'  ','ADDING CLOSE')
                bt(openb,closeb+1,curlist+[')'], level+1)

        bt(0,0, [],0)
        return result