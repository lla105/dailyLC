class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def isPalindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])  # Make a copy of path
                return
            
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    # Add the substring s[start:end+1] to the current path
                    path.append(s[start:end+1])
                    # Recurse with the next start index
                    backtrack(end + 1, path)
                    # Backtrack, remove the last element added
                    path.pop()
        
        backtrack(0, [])
        return result
