class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0=unvisited, 1=visiting, 2=visited
        arr = [0] * numCourses
        PR = prerequisites
        # build dictionary = { pre-req: [class1, class2, ...] }
        d = defaultdict(list)

        for i in range(len(PR)):
            d[PR[i][1]].append(PR[i][0])
        # print(d)
        self.isCycle = False

        def bfs(classnum):
            if arr[classnum] == 1: #is visiting
                self.isCycle = True
                return
            if arr[classnum] == 2: #is visisted, cycle detected
                return
            arr[classnum] = 1
            for eachClass in d[classnum]:
                bfs(eachClass)
            arr[classnum] = 2
            return

        for num in range(numCourses):
            if arr[num] == 0:
                bfs(num)
        return not self.isCycle