class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sdic = {}
        pdic = {}
        for i in range(len(p)):
            pdic[p[i]] = pdic.get(p[i], 0) + 1
        # print(pdic)
        result = []
        sdic = {}
        stack = deque()
        for i in range(len(s)):
            if i < len(p) - 1:
                stack.append(s[i])
                sdic[s[i]] = sdic.get(s[i], 0 ) + 1
                continue

            sdic[s[i]] = sdic.get(s[i], 0 ) + 1
            stack.append(s[i])
            # print(sdic, stack)
            # compare
            matches = True
            for char, count in pdic.items():
                if sdic.get(char) != count:
                    matches = False
            if matches :
                result.append(i-len(p)+1)
            temp = stack.popleft()
            # print('removing : ', sdic.pop(temp) )
            if temp in sdic and sdic.get(temp) > 1:
                sdic[temp] -= 1
            else:
                sdic.pop(temp)

        return result
        # result = []
        # p = sorted(p)
        # for i in range(len(s)-len(p)+1):
        #     temps = ''.join(sorted(s[i:i+len(p)]))
        #     # print(s[i:i+len(p)], temps)
        #     count = 0
        #     for j in range(len(p)):
        #         if temps[j] == p[j]:
        #             count+=1
        #     if count == len(p):
        #         result.append(i)

        # return result