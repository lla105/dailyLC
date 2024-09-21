class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        output = []

        def dfs( base ):
            newbase = base*10
            if newbase > n:
                return
            for i in range( newbase , newbase+10):
                if i>n :
                    continue
                output.append(i)
                dfs(i)
        
        for i in range(1,10):
            if i>n:
                continue
            output.append(i)
            dfs(i)

        return output