class Solution:
    def diffWaysToCompute(self, expression: str, level = 0) -> List[int]:
        res = []
        # ans = []
        for i in range(len(expression)):
            oper = expression[i]
            # if oper == "+" or oper == "-" or oper == "*":
            if oper in '+-*':
                sub_str1 = expression[0 : i]
                sub_str2 = expression[i + 1 : ]
                s1 = self.diffWaysToCompute(sub_str1, level+1)
                s2 = self.diffWaysToCompute(sub_str2, level+1)
                print(level*'  ', 's1:',s1, ' , s2:', s2)
                for i in s1:
                    for j in s2:
                        print(level*'  ', int(i),oper,int(j))
                        if oper == "*":
                            res.append(int(i) * int(j))
                        if oper == "+":
                            res.append(int(i) + int(j))
                        if oper == "-":
                            res.append(int(i) - int(j))

        print(level*'  ', 'res : ', res )
        if len(res) == 0:
            res.append(int(expression))
        # print(res)
        return res