class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            print(' called bt : ', target, path)
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            print('  entering for loop')
            for i in range(start, len(candidates)):
                print('    ', i)
                backtrack(i, target - candidates[i], path + [candidates[i]])
            print('  leaving for loop')
        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result