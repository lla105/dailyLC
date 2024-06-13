class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        PR = prerequisites
        for i in range(len(PR)):
            d[PR[i][1]].append(PR[i][0])
        # print(d)
        visited = [0] * numCourses

        def dfs(node):
            if visited[node] == 1: #being visited, cycle detected
                return False
            if visited[node] == 2: # node fully visited
                return True
            visited[node] = 1

            for neighbor in d[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2
            return True
        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(course):
                    return False

        return True