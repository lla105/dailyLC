class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = sorted(candidates)
        output = []
        def traverse( summ, arr, start_index ):
            if summ> target:
                return
            if summ==target:
                sorted_arr = sorted(arr)
                output.append( tuple(sorted_arr) )
                return 
            for i in range(start_index, len(c) ):
                if i>start_index and c[i]==c[i-1] :
                    continue
                traverse( summ+c[i], arr+[c[i]], i+1)
        traverse(0, [], 0)
        return output