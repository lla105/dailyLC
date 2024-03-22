def strToList(n):
    lst = []
    for i in range(len(n)):
        lst.append(n[i])
    return lst

def squareDaList(lst):
    for i in range(len(lst)):
        num = int(lst[i])
        lst[i] = int(num*num)
    return lst
 
def sumList(lst):
    summ = 0
    for i in range(len(lst)):
        summ += lst[i]
        # print(summ)
    return summ

class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        summ = 0
        # lst = str(n)
        lst = strToList(str(n))
        while summ!=1:
            lst = squareDaList(lst)
            summ = sumList(lst)
            if summ in s:
                return False
            s.add(summ)
            lst = strToList(str(summ))
            # print(">>>", summ)
        return True