class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prq = prerequisites
        # prq = [1,2],[2,3],[3,2]
        prq = prerequisites
        dic = defaultdict(list)
        for course, prereq in prq:
            dic[prereq].append(course)
        for i,v in dic.items():
            print('>> ', i,' -> ', v)
        self.output = True

        self.visited = set()
        self.done = set()

        def dfs( this_class ) :

            if this_class in self.visited:
                self.output = False
                return False
            if this_class in self.done :
                return True
            self.visited.add( this_class )

            classlist = dic[this_class]
            for eachclass in classlist :
                if not dfs( eachclass ):
                    return False
            self.visited.remove( this_class )
            self.done.add( this_class )
            return True 
            
        for i in range(numCourses) :
            if not dfs( i ):
                return False

        return True
