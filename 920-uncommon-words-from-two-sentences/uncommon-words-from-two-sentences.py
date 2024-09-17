class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        arr = s1 + ' ' + s2 + ' '
        # print('arr : ', arr) 
        d = {}
        word = ''
        for char in arr :
            if char == ' ':
                d[word] = d.get( word, 0) + 1
                word = ''
            else:
                word += char
        print(d)
        outputlist = []
        for i,v in d.items():
            if v==1:
                outputlist.append(i)
        return outputlist
        # word = ''
        # seen1 = set()
        # seen2 = set()
        # # for char in s1:
        # for i in range(len(s1)):
        #     char = s1[i]
        #     if char == ' ':
        #         seen1.add(word)
        #         word = ''
        #     elif i==len(s1)-1 :
        #         word+=char
        #         seen1.add(word)
        #     else:
        #         word += char
        # word = ''
        # # for char in s2:
        # for i in range(len(s2)):
        #     char = s2[i]
        #     if char == ' ':
        #         seen2.add(word)
        #         word = ''
        #     elif i==len(s2)-1:
        #         word+=char
        #         seen2.add(word)
        #     else:
        #         word += char
        # outputlist = []
        # print('seen1: ', seen1)
        # print('seen2: ', seen2)
        # for word in seen1:
        #     # print(word)
        #     if word not in seen2:
        #         outputlist.append(word)
        # for word in seen2:
        #     if word not in seen1:
        #         outputlist.append(word)
        # return outputlist