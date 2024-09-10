class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(speed)):
            cars.append( (position[i], speed[i]) )
        print('cars : ', cars)
        cars = sorted(cars, key=lambda x:x[0])
        print('sorted : ', cars)
        revcars = [] 
        for i in range(len(cars)-1,-1,-1):
            revcars.append(cars[i])
        cars = revcars
        stack = []
        for i in range(len(cars)):
            p = cars[i][0]
            s = cars[i][1]
            t = (target-p)/ s
            stack.append(t)
            if len(stack)>1 and stack[-2]>=stack[-1]:
                stack.pop()
        return len(stack)