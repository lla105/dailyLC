class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1temp = Counter(s1)
        s2temp = Counter(s2)
        print(len(s2))
        print(s1temp)
        print(s2temp)

        for i in range(0, len(s2)-len(s1)+1):
            # print(i, i+len(s1) , " --> ", s2[i : i+len(s1)])
            s2temp = Counter(s2[i:i+len(s1)])

            isPerm = True
            for j,v in s1temp.items():
                # print(s2temp.get(j))
                if s1temp[j]!=s2temp.get(j):
                    isPerm = False

            if isPerm:
                return True

        return False