class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        # print(f'target : {target}')
        # print(f'pairs : {pairs}')

        stack=[]
        for i in range(len(pairs)) :
            p = pairs[i][0]
            s = pairs[i][1]
            t = (target-p) / s
            # print(f'({p},{s}) : {t}')
            stack.append(t)
            if len(stack)>1 and stack[-2]>=stack[-1]:
                stack.pop()

        return len(stack)