class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(speed)):
            cars.append( (position[i], speed[i]) )
        print('cars : ', cars)
        cars = sorted(cars, key=lambda x:x[0], reverse=True)
        print('sorted : ', cars)

        stack = []
        for i in range(len(cars)):
            p = cars[i][0]
            s = cars[i][1]
            t = (target-p)/ s
            if not stack or t > stack[-1] :
                stack.append(t)
        return len(stack)