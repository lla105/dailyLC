class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        PR = prerequisites
        for i in range(len(PR)):
            d[PR[i][1]].append(PR[i][0])
        # print(d)
        visited = [0] * numCourses
        self.isCycle = False
        def dfs(node):
            if visited[node] == 1: #being visited, cycle detected
                self.isCycle = True
                return 
            if visited[node] == 2: # node fully visited
                return 
            visited[node] = 1

            for neighbor in d[node]:
                dfs(neighbor)
                # if not dfs(neighbor):
                #     return False
            visited[node] = 2
            return 
        for course in range(numCourses):
            if visited[course] == 0:
                dfs(course)
                # if not dfs(course):
                #     return False

        if self.isCycle:
            return False
        else:
            return True