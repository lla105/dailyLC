class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # for i in range(len(spaces)):
        #     index = spaces[i]+i
        #     s = s[:index] + " " + s[index:]
        # return s
        output = []
        spaceset = set(spaces)
        print(spaceset)
        for i in range(len(s)):
            char = s[i]
            if i in spaceset:
                output.append(' ')
            output.append(char)
        return ''.join(output)