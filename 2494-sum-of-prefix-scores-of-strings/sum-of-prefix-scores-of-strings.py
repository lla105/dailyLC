class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        dic = {}
        for i in range(len(words)):
            word = words[i]
            while word and len(word)>0:
                dic[word] = dic.get( word , 0 ) + 1
                word = word[:-1]
        # print(dic)
        output_list = []
        for i in range(len(words)):
            count = 0
            word = words[i]
            while word and len(word)>0 :
                if word in dic :
                    count += dic[word]
                word = word[:-1]
            output_list.append(count)
        return output_list