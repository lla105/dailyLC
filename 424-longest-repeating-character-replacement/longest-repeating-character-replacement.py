class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        highestfreq = 0
        longest = 0
        stack = deque()
        d = {}

        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
            highestfreq = max(highestfreq , d[s[i]])
            if k > len(stack) - highestfreq:
                stack.append(s[i])
            else:
                d[s[i - len(stack)]] -= 1
            # print(stack)
        return len(stack)

            # stack.append(s[i])
            # slen = len(stack)
            # if k < slen - highestfreq:
            #     rm = stack.popleft()
            #     d[rm] -= 1
            # else:
            #     slen += 1
            #     highestfreq = max(highestfreq , slen-highestfreq)

