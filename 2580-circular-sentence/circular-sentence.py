class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i in range(len(sentence)):
            char = sentence[i]
            # print(char)
            if i == len(sentence)-1:
                if char!=sentence[0] :
                    return False
                    continue
            if char == ' ':
                # print('is space : ', sentence[i-1:i+2])
                if sentence[i-1]!=sentence[i+1]:
                    return False
                continue
        return True
