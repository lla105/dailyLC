class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d ={}
        highest = 0
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i] , 0 ) + 1
            highest = max(highest, d[nums[i]])
        freq = set()
        dd = defaultdict(list)
        for i,v in d.items():
            dd[v].append(i)
            freq.add(v)
        print(d)
        print(dd, freq)
        freq = sorted(freq)
        print(freq)
        result = []
        for frequency in freq:
            sortedlist = sorted(dd[frequency] , reverse=True)
            for num in sortedlist:
                for _ in range(frequency):
                    result.append(num)
        return result