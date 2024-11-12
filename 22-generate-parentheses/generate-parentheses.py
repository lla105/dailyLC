class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def bt(openb, closeb, curlist, level):
            if closeb==openb and openb==n:
                result.append(''.join(curlist))
                return
            # if n>openb:
            if n>openb and n>closeb:
                bt(openb+1, closeb, curlist+['('], level+1)
            # if openb==n and openb>closeb:
            if openb<=n and openb>closeb:
                bt(openb,closeb+1,curlist+[')'], level+1)

        bt(0,0, [],0)
        return result