class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        totalsum = sum(skill)
        halflen = (len(skill))/2
        if len(skill) == 2:
            return skill[0] * skill[1]

        if halflen % 1 != 0 or (len(skill))%2!= 0 :
            return -1
        d = Counter(skill)
        pairsum = totalsum / halflen
        output = []
        for i in range(len(skill)) :
            num = int(skill[i])
            if d[num] <= 0:
                continue
            diff = int(pairsum - num)
            d[num] -= 1
            if d[diff] <= 0 :
                continue
            d[diff] -=1 
            output.append( (num,diff) )
        answer = 0
        print('??fffasdf?asdf')
        if not output or len(output) != halflen :
            return -1
        for num1,num2 in output:
            answer += (num1*num2)
        return answer
        