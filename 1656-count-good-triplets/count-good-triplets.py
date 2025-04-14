class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        i=0
        j=1
        k=2
        output = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    # print(i,j,k)
                    cond1 = abs(arr[i]-arr[j]) <=a
                    cond2 = abs(arr[j]-arr[k]) <=b
                    cond3 = abs(arr[k]-arr[i]) <=c
                    if cond1 and cond2 and cond3:
                        output+=1

        return output
