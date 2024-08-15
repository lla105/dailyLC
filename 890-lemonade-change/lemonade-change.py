class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        self.result = False
        d = { 5:0, 10:0, 20:0 }
        for i in range(len(bills)):
            bill = bills[i]
            print(f'{i} bill: {bill}')
            if bill==20:
                if d[5] < 3 and (d[10]<1 or d[5]<1):
                    print(' FALSE: bill=$20' , d)
                    return False
                if d[10]>0:
                    d[10] -= 1
                    d[5] -= 1
                else :
                    d[5] -=3 
                    if d[5] <0:
                        return False
            
            elif bill==10:
                if d[5]<1:
                    print( ' FALSE; bill=$10', d)
                    return False
                d[5]-=1
                d[10] += 1
            else:
                d[5] += 1
            print(d)
        return True