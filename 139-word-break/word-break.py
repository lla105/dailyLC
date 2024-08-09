class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]* (len(s)+1)
        dp[0] = True

        
        for i in range(len(s)):
            def printt(level, msg):
                # print(level*' ', msg)
                return

            if not dp[i] :
                continue
            for word in wordDict:
                printt(i, word)
                tail = i+len(word)
                if tail>len(s):
                    printt(i, ' 1) tail>=len(s)')
                    continue
                if word!=s[i:i+len(word)]:
                    printt(i, ' 2) word!=')
                    continue
                printt(i, ' 3)')
                dp[tail] = True
        print(dp)
        return dp[-1]

        # self.result = False
        # self.dp = [False] * (len(s)+1)
        # self.dp[0] = True
        # # print(self.dp)

        # def bt( sindex, level):
        #     def printt(msg):
        #         print(level *' ', msg)
        #     if sindex>=len(s):
        #         # printt(' END ')
        #         return
        #     # printt(f'bt stack: {sindex}, {s[sindex:]}')
        #     for i in range(len(wordDict)):
        #         word = wordDict[i]
        #         # print( ' looking at word : ', word)
        #         # printt(f' looking at word: {word}')
        #         if len(s)< sindex+len(word):
        #             # print('  len(s) <= s+len(word)' )
        #             # printt(f' len(s)={len(s)} <= s+len(word) {sindex}+{len(word)}. CONTINUE')
        #             continue
        #         if word != s[sindex:len(word) + sindex]:
        #             # print('  ', word, '=', s[sindex:len(word)])
        #             # printt( f'{word} = {s[sindex:sindex+len(word)]} -> CONTINUE')
        #             continue
        #         # print('MATCH!')
        #         self.dp[sindex+len(word)] = True
        #         bt(sindex+len(word), level+1)
        # bt(0, 0)
        # # print(self.dp)
        # return self.dp[-1]