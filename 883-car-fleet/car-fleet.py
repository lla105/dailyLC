class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append( (position[i], speed[i]) )
        pairs = sorted(pairs, reverse=True)
        print(f'{pairs}')
        stack=[]
        for i in range(len(pairs)):
            p = pairs[i][0]
            s = pairs[i][1]
            # print(p,s)
            t = (target-p)/s
            stack.append( t )
            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)