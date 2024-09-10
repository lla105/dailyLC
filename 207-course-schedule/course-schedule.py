class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the graph as an adjacency list
        graph = defaultdict(list)
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # Set to track courses that are fully processed (visited)
        visited = set()
        # Set to track courses in the current path (in the DFS call stack)
        current_path = set()
        
        # DFS function to detect cycles
        def dfs(course):
            if course in current_path:  # Cycle detected
                return False
            if course in visited:  # Already processed this course, no cycle
                return True
            
            # Add the course to the current path set
            current_path.add(course)
            
            # Explore all neighboring courses (prerequisites)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            # Remove the course from the current path and mark it as fully processed
            current_path.remove(course)
            visited.add(course)
            
            return True
        
        # Check each course
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True