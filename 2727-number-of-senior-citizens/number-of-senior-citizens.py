class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            # print(details[i][10:13])
            if int(details[i][11:13]) > 60:
                count+=1
        return count