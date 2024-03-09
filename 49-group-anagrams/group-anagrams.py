class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dic format : { 'ant' : ['nat', 'tan']}
        # dic['abc'].append('acb')
        # dic['abc'].append('abc')
        # if 'abc' in dic:
        #     print("yeaaaa")
        dic = defaultdict(list)

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
            # print(f"{i} , {v}")
            result.append(v)
        print(dic)
        return result