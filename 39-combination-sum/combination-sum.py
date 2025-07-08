class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        c = sorted(candidates)
        print(c)
        def traverse(index, arr ):
            if sum(arr) > target:
                return 
            if sum(arr) == target:
                output.append( tuple(arr) )
                return
            # print(arr)
            for i in range(index, len(c)):
                traverse(i, arr+[c[i]])
        traverse(0, [] )
        return output