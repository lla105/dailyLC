class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dic = defaultdict(list)
        dic = dict()
        for i in range(len(strs)):
            word = strs[i]
            sortedword = ''.join(sorted(word))
            if sortedword in dic:
                dic[sortedword].append(word)
            else:
                dic[sortedword] = [word]

        print("DIC TION ARY ;;:::: ", dic)
        result = []
        for i,v in dic.items():
            # print(i,v)
            result.append(v)

        return result

