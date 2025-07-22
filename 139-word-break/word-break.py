class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [ False ] * ( len(s)+1 )
        # cache[-1] = True
        self.output = False
        def traverse(start_idx):
            # print(f"traverse({start_idx})")
            if start_idx == len(s):
                # print(f" REACH BASE CASE")
                self.output = True
                return True
            for i in range(len(wordDict)):
                word = wordDict[i]
                # print(f">> word: {word}")
                if len(word)+start_idx > len(s):
                    # print(f">>> 1")
                    continue
                if word != s[start_idx: start_idx+len(word)] :
                    # print(f">>> {word} != {s[start_idx: start_idx+len(word)]}")
                    continue
                if cache[start_idx+len(word)] :
                    # print(f">>> IN CACHE ALREADY {word} != {s[start_idx: start_idx+len(word)]}")
                    continue
                # print(f"MATCH: {word} == {s[start_idx: start_idx+len(word)]}")
                cache[start_idx+len(word)] = True
                # print(cache)
                traverse(start_idx + len(word))
        traverse(0)
        return self.output


#abcde, wordDict = [ab,cd,a,bcd]
# cache_array = [f,t,t,f,t,f]
#ab -> cd 
#a -> bcd -> 

#catsandog
# base case: start_idx==len(s)
# word = wordDict[i]
#cats , [0:0+len(word)]
#   and , [4:4+len(word)]
#       og x
#dog
#sand
#and
#cat
#   sand
#       og x