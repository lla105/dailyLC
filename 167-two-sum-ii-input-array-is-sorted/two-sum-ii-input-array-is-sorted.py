class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print(f'numbers: {numbers}, target: {target}')
        d = {} #format : {value:index}
        for i in range(len(numbers)):
            num = numbers[i]
            diff = target-num
            print(f"diff : {diff}")
            if diff in d:
                return [d[diff]+1, i+1]
            d[num]=i
            print(f'>> {d}')
 
        