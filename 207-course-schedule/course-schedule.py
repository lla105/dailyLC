class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = defaultdict(list)
        for i, v in prerequisites:
            premap[i].append(v)

        visited = set()  # Nodes that have been fully processed
        visiting = set() # Nodes that are being visited in the current path
        
        def dfs(node):
            if node in visiting:
                return True  # Found a cycle
            if node in visited:
                return False # No cycle from this node
            
            visiting.add(node)
            for neighbor in premap[node]:
                if dfs(neighbor):
                    return True
            visiting.remove(node)
            visited.add(node)
            return False

        for n in range(numCourses):
            if dfs(n):
                return False

        return True