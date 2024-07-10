class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for i in range(len(logs)):
            if logs[i] == '../':
                if level > 0 :
                    level -= 1
            elif logs[i] == './':
                pass
            else:
                level += 1
        return level 
