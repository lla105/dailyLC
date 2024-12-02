class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        wordcount=1
        if len(sentence) < len(searchWord):
            return -1
        if sentence[:len(searchWord)] == searchWord:
            return 1
        for i in range(len(sentence)):
            if sentence[i]==" " and i+len(searchWord)<len(sentence):
                if sentence[i+1:i+len(searchWord)+1] == searchWord:
                    return wordcount+1
            if sentence[i]==" ":
                wordcount+=1
        return -1