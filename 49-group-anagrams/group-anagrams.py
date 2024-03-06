class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs)<=0:
            return [[""]]

        if len(strs)==1:
            return [strs]

        dic = defaultdict(list)
        for word in strs:
            sword = sorted(word)
            sword = ''.join(sword)
            if sword in dic:
                dic[sword].append(word)
            else :
                dic[sword] = [word]
        answer = []
        for key,value in dic.items():
            answer.append(value)

        return answer