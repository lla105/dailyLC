class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        pr = prerequisites
        for i in range(len(pr)):
            d[ pr[i][1] ].append( pr[i][0] )

        curpath = set()
        visited = set()
        def dfs( course ):
            if course in curpath :
                return False # found a cycle. BAD
            if course in visited:
                return True
            curpath.add( course )
            for neighbor in d[course] :
                if not dfs( neighbor ) :
                    return False
            curpath.remove( course )
            visited.add( course ) 
            return True
        for i in range(numCourses):
            temp = dfs(i)
            if not temp:
                return False
        return True