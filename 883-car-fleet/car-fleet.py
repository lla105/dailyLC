class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(speed)):
            cars.append( (position[i] , speed[i] ) )
        cars = sorted(cars, key=lambda x:x[0])
        print( 'cars : ', cars)
        stack = []
        for i in range( len(cars)-1,-1,-1 ):
            timeleft = ( target-cars[i][0]) / cars[i][1]
            if not stack:
                stack.append( timeleft )
                continue
            if stack[-1] < timeleft : #merge
                stack.append( timeleft )
            # else:
            #     stack[-1] = max(stack[-1] , timeleft)
        return len(stack)