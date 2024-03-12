class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair = sorted(pair(position, speed))
        length = len(position)
        pair = []
        for i in range(length):
            pair.append( (position[i], speed[i]) )
        pair = sorted(pair, reverse=True)
        # print(f'>> {pair}')

        stack = []
        for i in range(len(pair)):
            p = pair[i][0]
            s = pair[i][1]
            stack.append( (target-p) / s)
            # print(f'>>>>> {p}, {s} : {stack}')

            if len(stack)>=2 and stack[-1]<=stack[-2]: #merge
                # print(f'pop : {stack[-1]} >= {stack[-2]}')
                stack.pop()
        return len(stack)
        