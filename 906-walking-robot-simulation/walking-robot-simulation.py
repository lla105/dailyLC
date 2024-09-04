class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def getdistance( x, y ):
            xx = x*x
            yy = y*y
            tempsum = xx+yy
            return tempsum
        directions = [ (0,1), (1,0), (0,-1), (-1,0) ]

        dindex= 0 # facing north.
        maxdist = 0
        obstacle = set()
        for x,y in obstacles:
            obstacle.add( (x,y) )
        position = [0,0]
        for command in commands:
            if command > 0 :
                for _ in range(command):
                    xmove = position[0] + directions[dindex][0]
                    ymove = position[1] + directions[dindex][1]
                    if (xmove,ymove) in obstacle:
                        continue
                    else:
                        position[0] = xmove
                        position[1] = ymove
            elif command == -1:
                dindex += 1
            elif command == -2:
                dindex -= 1

            if dindex >= len(directions) :
                dindex = 0
            elif dindex < 0 :
                dindex = len(directions) - 1
            
            distance = getdistance( position[0] , position[1] )
            maxdist = max(maxdist, distance)
        print(position)
        return maxdist